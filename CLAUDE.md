# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Rudolf Steiner works reading platform with PDF/EPUB/DOCX import, German→Chinese translation (Google Translate), user credit system, and admin backend.

## Tech Stack

- **Backend**: Python 3.12, FastAPI, SQLAlchemy 2 (async + asyncpg), PostgreSQL
- **Frontend**: Next.js 16.2, TypeScript, Tailwind CSS 4, React 19
- **Deploy**: Docker Compose (nginx + backend + frontend), PostgreSQL runs separately as `steiner-postgres`
- **DB**: PostgreSQL, database `steiner_reader`. Credentials in `backend/.env` (`DATABASE_URL`)

## Dev Commands

```bash
# Backend (from backend/)
uvicorn app.main:app --reload --port 8000

# Frontend (from frontend/)
npm run dev          # Next.js dev server on port 3000

# Docker Compose (full stack)
docker-compose up -d
docker-compose restart backend   # restart just backend
```

There are no lint or test commands configured (no pytest, no jest, no eslint).

## Architecture

### Backend (`backend/app/`)

| File | Purpose |
|------|---------|
| `main.py` | FastAPI app, CORS (all origins), registers all routers |
| `config.py` | Pydantic `BaseSettings` from `.env` / environment |
| `db/database.py` | Async engine, `get_db()` session generator |
| `db/models.py` | ORM: `Book`, `Lecture`, `Paragraph`, `Sentence`, `LectureImage`, `TranslationJob`, `User` |
| `models/schemas.py` | Pydantic request/response schemas |

**Routers** (prefixes registered in `main.py`):

| Router | Prefix | Key responsibility |
|--------|--------|-------------------|
| `auth.py` | `/api/auth` | Register, login, JWT, change password/email. Exports `get_current_user`, `require_user`, `require_admin` |
| `admin.py` | `/api/admin` | User CRUD, credit set/add, reset password, toggle admin, lecture retranslation |
| `books.py` | `/api/books` | Book list/summary/groups, lecture content with paragraphs+sentences+images |
| `lectures.py` | `/api/lectures` | Lecture paragraphs with sentences, shared `_build_paragraph_response()` |
| `paragraphs.py` | `/api/paragraphs` | Sentences for a single paragraph |
| `translate.py` | `/api` | Start translation (POST), cost estimate, status polling. Background task, 20-sentence batches, 10 credits cost |
| `images.py` | `/api` | List images by book/lecture, serve image files from disk |
| `upload.py` | `/api` | PDF upload + parse + save. Only accepts `.pdf` |

**Services**:
- `pdf_parser.py` — Memory-optimized PDF parsing with pdfplumber. German lecture header detection regex, sentence/paragraph splitting. Returns `Book`/`Lecture`/`Paragraph`/`Sentence` dataclasses.
- `translator.py` — `deep-translator` GoogleTranslator. `translate_sentence_sync()`, `translate_sentence_async()`, batch translation with 300ms delay.

**Auth**: JWT with HS256, 7-day expiry. Tokens expected as `Authorization: Bearer <token>`. `python-jose` + `passlib[bcrypt]`.

### Frontend (`frontend/app/`)

| Path | Purpose |
|------|---------|
| `layout.tsx` | Root layout, Header, `lang="de"`, imports globals.css |
| `page.tsx` | Home with 3 view modes via `?view=` param: `group` (default), `grid`, `search` |
| `login/page.tsx` | Login/register tabs |
| `profile/page.tsx` | User info, change password/email, logout |
| `admin/page.tsx` | Full user management table with search, credit management, edit/delete |
| `upload/page.tsx` | Drag-and-drop file upload (accepts `.epub,.docx` but backend only handles `.pdf`) |
| `books/[bookId]/page.tsx` | Book TOC with hierarchical lecture tree (headings vs lectures) |
| `books/[bookId]/lectures/[lectureId]/page.tsx` | Reader with 3 modes: `de-zh` side-by-side, `de-only`, `zh-only`. Translate button, polling, image lightbox |
| `components/Header.tsx` | Nav with conditional admin/upload links, credits badge, login/logout |
| `components/GroupedBooksView.tsx` | Books grouped by GA decade (accordion) |
| `components/PaginatedBooksView.tsx` | Sortable paginated grid (24/page) |
| `components/SearchBooksView.tsx` | Debounced search (300ms) in paginated grid |

**API client** (`lib/api.ts`): All fetch wrappers with 12s timeout. JWT in `localStorage('steiner_token')`. User object in `localStorage('steiner_user')`. Dispatches `auth-changed` event on login/logout. Dev API proxied to `127.0.0.1:8000` via `next.config.ts` rewrites.

**Styles** (`globals.css`): Tailwind v4 (`@import "tailwindcss"`). Custom CSS vars for brand palette. Utility classes: `.card`, `.btn-primary`, `.btn-secondary`, `.page-container`, `.shimmer`.

## Data Model Notes

- `Lecture.level`: `"heading"` or `"lecture"` — headings have children via `parent_id`
- `LectureImage`: positioned inline via `after_paragraph_id` / `after_sentence_id`
- `User.is_admin`: `0` or `1` (int, not bool)
- Translation costs 10 credits per lecture, deducted on start

## Import Scripts (`scripts/`)

~33 Python scripts for batch import, translation fixes, and reimport. Key entry points:
- `import_ga_generic.py`, `import_ga_simple.py` — main PDF import with sentence splitting
- `epub_importer.py`, `epub_importer_pipe.py` — EPUB import
- `batch_import.py`, `batch_import_all.py` — bulk imports
- `data/pdf/` contains ~240 GA PDFs, `downloads/` has ~170 `.doc` source files
- `lecture_collections.txt` lists already-imported GA numbers

## Infrastructure

- **Production domain**: `https://steiner.3mudi.com` (Cloudflare CDN → origin `66.154.112.162`)
- **Origin server**: `66.154.112.162`, SSH as `root`
- **Backend**: systemd service `steiner-backend` — uvicorn on `127.0.0.1:8000`
- **Frontend**: systemd service `steiner-frontend` — Next.js on `127.0.0.1:3000`
- **Nginx**: reverse proxy on origin, `/api/*` → `127.0.0.1:8000`, `/*` → `127.0.0.1:3000`, SSL via Let's Encrypt
- **PostgreSQL**: runs locally on origin as user `steiner`, DB `steiner_reader`
- Backend `IMAGES_DIR` is hardcoded to `/opt/steiner-reader/images` in `images.py`.
- Logs: `journalctl -u steiner-backend/frontend`, error logs at `/var/log/steiner-reader/`

### Frontend API URL Configuration

`api.ts` uses `NEXT_PUBLIC_API_URL || ''` as base URL. MUST be empty in production so the browser uses relative paths (`/api/...`) through the nginx proxy. Setting it to an absolute URL (e.g., `http://66.154.112.162:8000`) will break the site due to mixed-content blocking (HTTPS page → HTTP API).

- `.env` — `NEXT_PUBLIC_API_URL=` (empty, correct)
- `.env.local` — MUST also be empty; takes precedence over `.env`
- Dev: `next.config.ts` rewrites `/api/:path*` → `http://127.0.0.1:8000/api/:path*`

### Deploy Commands

```bash
# Backend
rsync -avz --exclude='__pycache__' --exclude='*.pyc' --exclude='.env' backend/ root@66.154.112.162:/opt/steiner-reader/backend/
ssh root@66.154.112.162 "systemctl restart steiner-backend.service"

# Frontend
rsync -avz --exclude='node_modules' --exclude='.next' frontend/ root@66.154.112.162:/opt/steiner-reader/frontend/
ssh root@66.154.112.162 "cd /opt/steiner-reader/frontend && npm run build && systemctl restart steiner-frontend.service"
```

## Key Warnings

- **Next.js 16**: This is a very new version. The frontend `AGENTS.md` warns API differences from older Next.js. Check `node_modules/next/dist/docs/` before writing Next.js code.
- **`book_images` table**: `images.py` queries a `book_images` table with raw SQL — this table is NOT defined in the ORM (`models.py` only has `lecture_images`). It may only exist in production.
- **No tests exist** anywhere in the project.
- **Frontend/backend upload mismatch**: Frontend accepts `.epub,.docx` but backend `upload.py` only handles `.pdf`.
- **CORS** is wide open (`allow_origins=["*"]`) — intentional for current deployment but noted as TODO.
- `python-jose`, `passlib`, `bcrypt` are used in auth but may not be explicitly listed in `requirements.txt`.

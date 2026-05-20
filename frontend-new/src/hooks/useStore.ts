import { create } from 'zustand';
import type { BookSummary, User } from '../types';

interface AppState {
  user: User | null;
  setUser: (user: User | null) => void;
  clearUser: () => void;
  books: BookSummary[];
  setBooks: (books: BookSummary[]) => void;
  isLoading: boolean;
  setIsLoading: (loading: boolean) => void;
  searchQuery: string;
  setSearchQuery: (query: string) => void;
  viewMode: 'group' | 'grid' | 'search';
  setViewMode: (mode: 'group' | 'grid' | 'search') => void;
}

export const useStore = create<AppState>((set) => ({
  user: null,
  setUser: (user) => set({ user }),
  clearUser: () => set({ user: null }),
  books: [],
  setBooks: (books) => set({ books }),
  isLoading: false,
  setIsLoading: (loading) => set({ isLoading: loading }),
  searchQuery: '',
  setSearchQuery: (query) => set({ searchQuery: query }),
  viewMode: 'group',
  setViewMode: (mode) => set({ viewMode: mode }),
}));

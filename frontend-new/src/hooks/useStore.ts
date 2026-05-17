import { create } from 'zustand';
import type { Book, User } from '../types';

interface AppState {
  user: User | null;
  setUser: (user: User | null) => void;
  books: Book[];
  setBooks: (books: Book[]) => void;
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
  books: [],
  setBooks: (books) => set({ books }),
  isLoading: false,
  setIsLoading: (loading) => set({ isLoading: loading }),
  searchQuery: '',
  setSearchQuery: (query) => set({ searchQuery: query }),
  viewMode: 'group',
  setViewMode: (mode) => set({ viewMode: mode }),
}));

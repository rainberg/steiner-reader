import type { Metadata } from 'next';
import './globals.css';
import Header from './components/Header';

export const metadata: Metadata = {
  title: 'Steiner Reader — 施泰纳著作阅读平台',
  description: '阅读和翻译鲁道夫·施泰纳（Rudolf Steiner）人智学著作',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="de">
      <body className="antialiased">
        <Header />
        {children}
      </body>
    </html>
  );
}

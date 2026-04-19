import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Steiner Reader — 施泰纳著作阅读平台',
  description: '阅读和翻译鲁道夫·施泰纳（Rudolf Steiner）人智学著作',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="de">
      <body className="antialiased">{children}</body>
    </html>
  );
}

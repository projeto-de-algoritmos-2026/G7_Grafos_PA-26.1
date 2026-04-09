import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "G7 Grafos - Ordenação Topológica",
  description: "Aprenda como Grafos Direcionados Acíclicos funcionam através de receitas culinárias.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}

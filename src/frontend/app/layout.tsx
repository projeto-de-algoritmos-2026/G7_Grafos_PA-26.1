import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "TopoChef",
  description: "site para desenvolver as receitas do seu jeito e aprender sobre grafos aciclicos",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-screen flex flex-col w-full text-white">
        <header className="bg-blue-950 flex flex-col justify-center items-center h-[125px] w-full gap-2">
          <h1 className="text-3xl font-bold">TopoChef</h1>
          <h2 className="px-5 text-center" >Aprenda ordenação topológica através de receitas!</h2>
        </header>
        <main className="w-full flex-1 bg-gray-900 flex flex-col justify-center items-center gap-10 py-10">
          {children}
        </main>
      </body>
    </html>
  );
}

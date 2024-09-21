import localFont from 'next/font/local';
import './globals.css';

const interItalic = localFont({
    src: './fonts/Inter-Italic-VariableFont_opsz,wght.ttf',
    variable: '--font-inter-italic',
    weight: '100 900',
    style: 'italic',
});

const interNormal = localFont({
    src: './fonts/Inter-VariableFont_opsz,wght.ttf',
    variable: '--font-inter-normal',
    weight: '100 900',
    style: 'normal',
});

export const metadata = {
    title: 'Home - Streaming platform',
    description: 'Home page of streaming platform',
};

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body className={`${interItalic.variable} ${interNormal.variable}`}>
                {children}
            </body>
        </html>
    );
}

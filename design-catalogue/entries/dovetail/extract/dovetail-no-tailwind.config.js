/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(43, 86%, 97%)',
            '100': 'hsl(43, 86%, 94%)',
            '200': 'hsl(43, 86%, 86%)',
            '300': 'hsl(43, 86%, 76%)',
            '400': 'hsl(43, 86%, 64%)',
            '500': 'hsl(43, 86%, 50%)',
            '600': 'hsl(43, 86%, 40%)',
            '700': 'hsl(43, 86%, 32%)',
            '800': 'hsl(43, 86%, 24%)',
            '900': 'hsl(43, 86%, 16%)',
            '950': 'hsl(43, 86%, 10%)',
            DEFAULT: '#f9e5b1'
        },
        secondary: {
            '50': 'hsl(32, 32%, 97%)',
            '100': 'hsl(32, 32%, 94%)',
            '200': 'hsl(32, 32%, 86%)',
            '300': 'hsl(32, 32%, 76%)',
            '400': 'hsl(32, 32%, 64%)',
            '500': 'hsl(32, 32%, 50%)',
            '600': 'hsl(32, 32%, 40%)',
            '700': 'hsl(32, 32%, 32%)',
            '800': 'hsl(32, 32%, 24%)',
            '900': 'hsl(32, 32%, 16%)',
            '950': 'hsl(32, 32%, 10%)',
            DEFAULT: '#ede5dc'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#1d1e21',
        'neutral-200': '#000000',
        'neutral-300': '#fef9f3',
        background: '#f9e5b1',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Lausanne',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '28px',
                letterSpacing: '0.2px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '29.92px',
                letterSpacing: '0.11008px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '28px',
                letterSpacing: '0.2px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '48px',
                letterSpacing: '-0.16px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '56.16px',
                letterSpacing: '-0.24px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '72px',
                letterSpacing: '-0.72px'
            }
        ]
    },
    spacing: {
        '20': '40px',
        '28': '56px',
        '36': '72px',
        '40': '80px',
        '45': '90px',
        '56': '112px',
        '80': '160px',
        '155': '310px',
        '187': '374px',
        '3px': '3px',
        '65px': '65px',
        '127px': '127px'
    },
    borderRadius: {
        lg: '16px',
        xl: '24px',
        full: '9999px'
    },
    screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1536px'
    },
    transitionDuration: {
        '150': '0.15s',
        '200': '0.2s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.4, 0, 0.2, 1)'
    },
    container: {
        center: true,
        padding: '32px'
    },
    maxWidth: {
        container: '1440px'
    }
},
  },
};

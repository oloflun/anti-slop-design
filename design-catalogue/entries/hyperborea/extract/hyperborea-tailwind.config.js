/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(20, 100%, 97%)',
            '100': 'hsl(20, 100%, 94%)',
            '200': 'hsl(20, 100%, 86%)',
            '300': 'hsl(20, 100%, 76%)',
            '400': 'hsl(20, 100%, 64%)',
            '500': 'hsl(20, 100%, 50%)',
            '600': 'hsl(20, 100%, 40%)',
            '700': 'hsl(20, 100%, 32%)',
            '800': 'hsl(20, 100%, 24%)',
            '900': 'hsl(20, 100%, 16%)',
            '950': 'hsl(20, 100%, 10%)',
            DEFAULT: '#ff5c0b'
        },
        secondary: {
            '50': 'hsl(359, 93%, 97%)',
            '100': 'hsl(359, 93%, 94%)',
            '200': 'hsl(359, 93%, 86%)',
            '300': 'hsl(359, 93%, 76%)',
            '400': 'hsl(359, 93%, 64%)',
            '500': 'hsl(359, 93%, 50%)',
            '600': 'hsl(359, 93%, 40%)',
            '700': 'hsl(359, 93%, 32%)',
            '800': 'hsl(359, 93%, 24%)',
            '900': 'hsl(359, 93%, 16%)',
            '950': 'hsl(359, 93%, 10%)',
            DEFAULT: '#730405'
        },
        accent: {
            '50': 'hsl(36, 43%, 97%)',
            '100': 'hsl(36, 43%, 94%)',
            '200': 'hsl(36, 43%, 86%)',
            '300': 'hsl(36, 43%, 76%)',
            '400': 'hsl(36, 43%, 64%)',
            '500': 'hsl(36, 43%, 50%)',
            '600': 'hsl(36, 43%, 40%)',
            '700': 'hsl(36, 43%, 32%)',
            '800': 'hsl(36, 43%, 24%)',
            '900': 'hsl(36, 43%, 16%)',
            '950': 'hsl(36, 43%, 10%)',
            DEFAULT: '#e3d2b8'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#000102',
        background: '#000102',
        foreground: '#e3d2b8'
    },
    fontFamily: {
        body: [
            'Noto Serif JP',
            'sans-serif'
        ],
        heading: [
            'Italiana',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: '20px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '24.375px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '17': [
            '17px',
            {
                lineHeight: '28.05px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '28px'
            }
        ],
        '19': [
            '19px',
            {
                lineHeight: '29.45px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '32px',
                letterSpacing: '-0.12px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '37.5px',
                letterSpacing: '-0.15px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '48px',
                letterSpacing: '-0.24px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '60px',
                letterSpacing: '-0.3px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '58.88px',
                letterSpacing: '-0.704px'
            }
        ],
        '140.8': [
            '140.8px',
            {
                lineHeight: '129.536px',
                letterSpacing: '-0.704px'
            }
        ],
        '89.6': [
            '89.6px',
            {
                lineHeight: '85.12px',
                letterSpacing: '-0.448px'
            }
        ],
        '69.12': [
            '69.12px',
            {
                lineHeight: '69.12px',
                letterSpacing: '-0.3456px'
            }
        ],
        '58.88': [
            '58.88px',
            {
                lineHeight: '58.88px',
                letterSpacing: '-0.2944px'
            }
        ]
    },
    spacing: {
        '1': '4px',
        '12': '48px',
        '14': '56px',
        '20': '80px',
        '24': '96px',
        '28': '112px',
        '44': '176px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '150': '0.15s',
        '500': '0.5s',
        '1200': '1.2s',
        '1400': '1.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.16, 1, 0.3, 1)'
    },
    container: {
        center: true,
        padding: '32px'
    },
    maxWidth: {
        container: '1480px'
    }
},
  },
};

/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(8, 86%, 97%)',
            '100': 'hsl(8, 86%, 94%)',
            '200': 'hsl(8, 86%, 86%)',
            '300': 'hsl(8, 86%, 76%)',
            '400': 'hsl(8, 86%, 64%)',
            '500': 'hsl(8, 86%, 50%)',
            '600': 'hsl(8, 86%, 40%)',
            '700': 'hsl(8, 86%, 32%)',
            '800': 'hsl(8, 86%, 24%)',
            '900': 'hsl(8, 86%, 16%)',
            '950': 'hsl(8, 86%, 10%)',
            DEFAULT: '#400d05'
        },
        secondary: {
            '50': 'hsl(42, 42%, 97%)',
            '100': 'hsl(42, 42%, 94%)',
            '200': 'hsl(42, 42%, 86%)',
            '300': 'hsl(42, 42%, 76%)',
            '400': 'hsl(42, 42%, 64%)',
            '500': 'hsl(42, 42%, 50%)',
            '600': 'hsl(42, 42%, 40%)',
            '700': 'hsl(42, 42%, 32%)',
            '800': 'hsl(42, 42%, 24%)',
            '900': 'hsl(42, 42%, 16%)',
            '950': 'hsl(42, 42%, 10%)',
            DEFAULT: '#ede5d3'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#020201',
        'neutral-200': '#191915',
        background: '#ede5d3',
        foreground: '#020201'
    },
    fontFamily: {
        sans: [
            'Cardo',
            'sans-serif'
        ],
        body: [
            'PT Mono',
            'sans-serif'
        ]
    },
    fontSize: {
        '15': [
            '15px',
            {
                lineHeight: '20.625px'
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
                lineHeight: '26.35px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '32px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '36px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '40px'
            }
        ],
        '88': [
            '88px',
            {
                lineHeight: '61.6px'
            }
        ],
        '115.2': [
            '115.2px',
            {
                lineHeight: '105.984px',
                letterSpacing: '-2.304px'
            }
        ],
        '89.6': [
            '89.6px',
            {
                lineHeight: '83.328px'
            }
        ],
        '53.76': [
            '53.76px',
            {
                lineHeight: '56.9856px'
            }
        ],
        '51.2': [
            '51.2px',
            {
                lineHeight: '53.248px'
            }
        ],
        '10.5': [
            '10.5px',
            {
                lineHeight: '15.75px',
                letterSpacing: '2.31px'
            }
        ]
    },
    spacing: {
        '1': '4px',
        '24': '96px',
        '28': '112px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
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

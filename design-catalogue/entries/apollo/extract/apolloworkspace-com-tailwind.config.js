/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(14, 78%, 97%)',
            '100': 'hsl(14, 78%, 94%)',
            '200': 'hsl(14, 78%, 86%)',
            '300': 'hsl(14, 78%, 76%)',
            '400': 'hsl(14, 78%, 64%)',
            '500': 'hsl(14, 78%, 50%)',
            '600': 'hsl(14, 78%, 40%)',
            '700': 'hsl(14, 78%, 32%)',
            '800': 'hsl(14, 78%, 24%)',
            '900': 'hsl(14, 78%, 16%)',
            '950': 'hsl(14, 78%, 10%)',
            DEFAULT: '#e97451'
        },
        secondary: {
            '50': 'hsl(14, 76%, 97%)',
            '100': 'hsl(14, 76%, 94%)',
            '200': 'hsl(14, 76%, 86%)',
            '300': 'hsl(14, 76%, 76%)',
            '400': 'hsl(14, 76%, 64%)',
            '500': 'hsl(14, 76%, 50%)',
            '600': 'hsl(14, 76%, 40%)',
            '700': 'hsl(14, 76%, 32%)',
            '800': 'hsl(14, 76%, 24%)',
            '900': 'hsl(14, 76%, 16%)',
            '950': 'hsl(14, 76%, 10%)',
            DEFAULT: '#2d0f06'
        },
        accent: {
            '50': 'hsl(49, 45%, 97%)',
            '100': 'hsl(49, 45%, 94%)',
            '200': 'hsl(49, 45%, 86%)',
            '300': 'hsl(49, 45%, 76%)',
            '400': 'hsl(49, 45%, 64%)',
            '500': 'hsl(49, 45%, 50%)',
            '600': 'hsl(49, 45%, 40%)',
            '700': 'hsl(49, 45%, 32%)',
            '800': 'hsl(49, 45%, 24%)',
            '900': 'hsl(49, 45%, 16%)',
            '950': 'hsl(49, 45%, 10%)',
            DEFAULT: '#918037'
        },
        'neutral-50': '#f9f8f0',
        'neutral-100': '#0c0503',
        'neutral-200': '#6f675e',
        'neutral-300': '#e1dccf',
        background: '#e1dccf',
        foreground: '#3c261c'
    },
    fontFamily: {
        sans: [
            'Mona Sans',
            'sans-serif'
        ],
        heading: [
            'paradigm-pro',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '16px',
                letterSpacing: '1.68px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '20px',
                letterSpacing: '1.96px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '29.25px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '33px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '58.8px',
                letterSpacing: '0.56px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '75.6px',
                letterSpacing: '0.72px'
            }
        ]
    },
    spacing: {
        '2': '8px',
        '16': '64px',
        '28': '112px',
        '207px': '207px'
    },
    transitionDuration: {
        '150': '0.15s',
        '300': '0.3s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.22, 1, 0.36, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '100%'
    }
},
  },
};

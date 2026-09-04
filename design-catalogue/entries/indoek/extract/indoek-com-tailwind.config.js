/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(210, 80%, 97%)',
            '100': 'hsl(210, 80%, 94%)',
            '200': 'hsl(210, 80%, 86%)',
            '300': 'hsl(210, 80%, 76%)',
            '400': 'hsl(210, 80%, 64%)',
            '500': 'hsl(210, 80%, 50%)',
            '600': 'hsl(210, 80%, 40%)',
            '700': 'hsl(210, 80%, 32%)',
            '800': 'hsl(210, 80%, 24%)',
            '900': 'hsl(210, 80%, 16%)',
            '950': 'hsl(210, 80%, 10%)',
            DEFAULT: '#135eab'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        background: '#efebe3',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Calibre',
            'sans-serif'
        ],
        body: [
            'GTStandard-M',
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
                lineHeight: '28px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '28.8px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '33.6px'
            }
        ],
        '34': [
            '34px',
            {
                lineHeight: '34px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '40px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '64px'
            }
        ]
    },
    spacing: {
        '0': '4px',
        '1': '80px',
        '2': '101px',
        '3': '130px',
        '4': '144px',
        '5': '163px',
        '6': '185px',
        '7': '208px',
        '8': '273px'
    },
    borderRadius: {
        md: '8px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0) 0px 0px 0px 1000px inset'
    },
    screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px'
    },
    transitionDuration: {
        '150': '0.15s',
        '300': '0.3s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.4, 0, 0.2, 1)',
        default: 'ease'
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

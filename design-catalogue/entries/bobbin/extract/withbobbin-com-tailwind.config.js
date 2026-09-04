/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(56, 94%, 97%)',
            '100': 'hsl(56, 94%, 94%)',
            '200': 'hsl(56, 94%, 86%)',
            '300': 'hsl(56, 94%, 76%)',
            '400': 'hsl(56, 94%, 64%)',
            '500': 'hsl(56, 94%, 50%)',
            '600': 'hsl(56, 94%, 40%)',
            '700': 'hsl(56, 94%, 32%)',
            '800': 'hsl(56, 94%, 24%)',
            '900': 'hsl(56, 94%, 16%)',
            '950': 'hsl(56, 94%, 10%)',
            DEFAULT: '#fbf27e'
        },
        secondary: {
            '50': 'hsl(34, 30%, 97%)',
            '100': 'hsl(34, 30%, 94%)',
            '200': 'hsl(34, 30%, 86%)',
            '300': 'hsl(34, 30%, 76%)',
            '400': 'hsl(34, 30%, 64%)',
            '500': 'hsl(34, 30%, 50%)',
            '600': 'hsl(34, 30%, 40%)',
            '700': 'hsl(34, 30%, 32%)',
            '800': 'hsl(34, 30%, 24%)',
            '900': 'hsl(34, 30%, 16%)',
            '950': 'hsl(34, 30%, 10%)',
            DEFAULT: '#f7f4f0'
        },
        accent: {
            '50': 'hsl(56, 90%, 97%)',
            '100': 'hsl(56, 90%, 94%)',
            '200': 'hsl(56, 90%, 86%)',
            '300': 'hsl(56, 90%, 76%)',
            '400': 'hsl(56, 90%, 64%)',
            '500': 'hsl(56, 90%, 50%)',
            '600': 'hsl(56, 90%, 40%)',
            '700': 'hsl(56, 90%, 32%)',
            '800': 'hsl(56, 90%, 24%)',
            '900': 'hsl(56, 90%, 16%)',
            '950': 'hsl(56, 90%, 10%)',
            DEFAULT: '#faf39b'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#70685c',
        'neutral-300': '#544e45',
        'neutral-400': '#8c8273',
        'neutral-500': '#a39b8f',
        'neutral-600': '#cdc6bc',
        'neutral-700': '#2a241d',
        'neutral-800': '#413c33',
        'neutral-900': '#e8e4de',
        background: '#000000',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'GT Standard',
            'sans-serif'
        ],
        heading: [
            'GT Alpina',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '12px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '21px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '26px',
                letterSpacing: '-0.5px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '36px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '35.2px',
                letterSpacing: '-0.8px'
            }
        ],
        '34': [
            '34px',
            {
                lineHeight: '37.4px',
                letterSpacing: '-0.85px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '51.84px',
                letterSpacing: '-1.2px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '66px',
                letterSpacing: '-1.5px'
            }
        ]
    },
    spacing: {
        '0': '1px',
        '1': '51px',
        '2': '56px',
        '3': '74px',
        '4': '80px',
        '5': '89px',
        '6': '107px',
        '7': '120px',
        '8': '137px',
        '9': '150px',
        '10': '160px',
        '11': '200px',
        '12': '285px',
        '13': '290px',
        '14': '330px',
        '15': '343px'
    },
    borderRadius: {
        sm: '5px',
        lg: '14px',
        xl: '24px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px',
        lg: 'rgba(250, 177, 47, 0.15) 0px 7px 15px 0px, rgba(250, 177, 47, 0.13) 0px 27px 27px 0px, rgba(250, 177, 47, 0.08) 0px 61px 37px 0px'
    },
    screens: {
        sm: '640px',
        md: '768px',
        '860px': '860px',
        lg: '960px',
        '1100px': '1100px'
    },
    transitionDuration: {
        '150': '0.15s',
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '350': '0.35s',
        '400': '0.4s',
        '450': '0.45s',
        '500': '0.5s',
        '600': '0.6s',
        '700': '0.7s',
        '8000': '8s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.22, 1, 0.36, 1)',
        linear: 'linear',
        default: 'ease'
    },
    container: {
        center: true,
        padding: '20px'
    },
    maxWidth: {
        container: '1512px'
    }
},
  },
};

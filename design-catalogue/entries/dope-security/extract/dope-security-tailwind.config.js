/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(359, 54%, 97%)',
            '100': 'hsl(359, 54%, 94%)',
            '200': 'hsl(359, 54%, 86%)',
            '300': 'hsl(359, 54%, 76%)',
            '400': 'hsl(359, 54%, 64%)',
            '500': 'hsl(359, 54%, 50%)',
            '600': 'hsl(359, 54%, 40%)',
            '700': 'hsl(359, 54%, 32%)',
            '800': 'hsl(359, 54%, 24%)',
            '900': 'hsl(359, 54%, 16%)',
            '950': 'hsl(359, 54%, 10%)',
            DEFAULT: '#edc3c4'
        },
        secondary: {
            '50': 'hsl(200, 23%, 97%)',
            '100': 'hsl(200, 23%, 94%)',
            '200': 'hsl(200, 23%, 86%)',
            '300': 'hsl(200, 23%, 76%)',
            '400': 'hsl(200, 23%, 64%)',
            '500': 'hsl(200, 23%, 50%)',
            '600': 'hsl(200, 23%, 40%)',
            '700': 'hsl(200, 23%, 32%)',
            '800': 'hsl(200, 23%, 24%)',
            '900': 'hsl(200, 23%, 16%)',
            '950': 'hsl(200, 23%, 10%)',
            DEFAULT: '#f7f9fa'
        },
        accent: {
            '50': 'hsl(273, 100%, 97%)',
            '100': 'hsl(273, 100%, 94%)',
            '200': 'hsl(273, 100%, 86%)',
            '300': 'hsl(273, 100%, 76%)',
            '400': 'hsl(273, 100%, 64%)',
            '500': 'hsl(273, 100%, 50%)',
            '600': 'hsl(273, 100%, 40%)',
            '700': 'hsl(273, 100%, 32%)',
            '800': 'hsl(273, 100%, 24%)',
            '900': 'hsl(273, 100%, 16%)',
            '950': 'hsl(273, 100%, 10%)',
            DEFAULT: '#af50ff'
        },
        'neutral-50': '#f0f0f0',
        'neutral-100': '#000000',
        'neutral-200': '#090909',
        'neutral-300': '#333333',
        'neutral-400': '#475467',
        'neutral-500': '#344054',
        'neutral-600': '#dae0e8',
        'neutral-700': '#d0d5dd',
        'neutral-800': '#878787',
        background: '#090909',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Whyte Inktrap',
            'sans-serif'
        ],
        mono: [
            'Whyte Inktrap Mono',
            'sans-serif'
        ],
        body: [
            'Karla',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '0px'
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
                lineHeight: 'normal'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px',
                letterSpacing: '0.08px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '36px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '33.6px',
                letterSpacing: '-0.28px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '38.4px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '40px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '57.6px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '57.6px',
                letterSpacing: '12.8px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '72px',
                letterSpacing: '-5.6px'
            }
        ],
        '88': [
            '88px',
            {
                lineHeight: '70.4px',
                letterSpacing: '-2.64px'
            }
        ],
        '18.4': [
            '18.4px',
            {
                lineHeight: '24.84px',
                letterSpacing: '0.12px'
            }
        ],
        '13.6': [
            '13.6px',
            {
                lineHeight: '19.04px',
                letterSpacing: '1.12px'
            }
        ],
        '11.2': [
            '11.2px',
            {
                lineHeight: '11.2px'
            }
        ]
    },
    spacing: {
        '12': '24px',
        '16': '32px',
        '19': '38px',
        '32': '64px',
        '36': '72px',
        '40': '80px',
        '48': '96px',
        '64': '128px',
        '68': '136px',
        '80': '160px',
        '104': '208px',
        '1px': '1px',
        '45px': '45px'
    },
    borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '11px',
        xl: '24px',
        full: '1584px'
    },
    boxShadow: {
        xs: 'rgba(16, 24, 40, 0.05) 0px 1px 2px 0px',
        sm: 'rgba(0, 0, 0, 0.25) 0px 3.2px 3.2px 0px',
        lg: 'rgba(0, 0, 0, 0.08) 0px 12px 16px -4px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px'
    },
    screens: {
        sm: '480px',
        lg: '992px',
        xl: '1280px',
        '1440px': '1440px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '300': '0.3s',
        '600': '0.6s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.165, 0.84, 0.44, 1)'
    },
    container: {
        center: true,
        padding: '64px'
    },
    maxWidth: {
        container: '2240px'
    }
},
  },
};

/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(240, 100%, 97%)',
            '100': 'hsl(240, 100%, 94%)',
            '200': 'hsl(240, 100%, 86%)',
            '300': 'hsl(240, 100%, 76%)',
            '400': 'hsl(240, 100%, 64%)',
            '500': 'hsl(240, 100%, 50%)',
            '600': 'hsl(240, 100%, 40%)',
            '700': 'hsl(240, 100%, 32%)',
            '800': 'hsl(240, 100%, 24%)',
            '900': 'hsl(240, 100%, 16%)',
            '950': 'hsl(240, 100%, 10%)',
            DEFAULT: '#0000ee'
        },
        secondary: {
            '50': 'hsl(4, 100%, 97%)',
            '100': 'hsl(4, 100%, 94%)',
            '200': 'hsl(4, 100%, 86%)',
            '300': 'hsl(4, 100%, 76%)',
            '400': 'hsl(4, 100%, 64%)',
            '500': 'hsl(4, 100%, 50%)',
            '600': 'hsl(4, 100%, 40%)',
            '700': 'hsl(4, 100%, 32%)',
            '800': 'hsl(4, 100%, 24%)',
            '900': 'hsl(4, 100%, 16%)',
            '950': 'hsl(4, 100%, 10%)',
            DEFAULT: '#ff5f54'
        },
        accent: {
            '50': 'hsl(41, 100%, 97%)',
            '100': 'hsl(41, 100%, 94%)',
            '200': 'hsl(41, 100%, 86%)',
            '300': 'hsl(41, 100%, 76%)',
            '400': 'hsl(41, 100%, 64%)',
            '500': 'hsl(41, 100%, 50%)',
            '600': 'hsl(41, 100%, 40%)',
            '700': 'hsl(41, 100%, 32%)',
            '800': 'hsl(41, 100%, 24%)',
            '900': 'hsl(41, 100%, 16%)',
            '950': 'hsl(41, 100%, 10%)',
            DEFAULT: '#ffbe32'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#1a1a1a',
        'neutral-300': '#5d5d5d',
        'neutral-400': '#464646',
        'neutral-500': '#737373',
        'neutral-600': '#242424',
        'neutral-700': '#2e2e2e',
        'neutral-800': '#ededed',
        'neutral-900': '#8c8c8c',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter Display',
            'sans-serif'
        ],
        body: [
            'Instrument Serif',
            'sans-serif'
        ],
        font2: [
            'Inter',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '14px',
                letterSpacing: '-0.2px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: 'normal'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '16.2918px',
                letterSpacing: '-0.59px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18.2px',
                letterSpacing: '-0.56px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '23.4px',
                letterSpacing: '-0.36px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: 'normal'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '26.4px',
                letterSpacing: '-0.8px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '31.2px',
                letterSpacing: '-0.52px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '33.6px',
                letterSpacing: '-0.56px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '39.6px',
                letterSpacing: '-0.72px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '48px',
                letterSpacing: '-1.44px'
            }
        ],
        '90': [
            '90px',
            {
                lineHeight: '90px',
                letterSpacing: '-4.5px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '100px',
                letterSpacing: '-7px'
            }
        ],
        '120': [
            '120px',
            {
                lineHeight: '120px',
                letterSpacing: '-8.4px'
            }
        ]
    },
    spacing: {
        '6': '24px',
        '7': '28px',
        '8': '32px',
        '10': '40px',
        '16': '64px',
        '20': '80px',
        '25': '100px',
        '30': '120px',
        '75': '300px',
        '1px': '1px'
    },
    borderRadius: {
        xs: '1px',
        sm: '4px',
        md: '8px',
        lg: '15px',
        xl: '24px',
        full: '100px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '810px'
    },
    transitionDuration: {
        '400': '0.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.44, 0, 0.56, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '700px'
    }
},
  },
};

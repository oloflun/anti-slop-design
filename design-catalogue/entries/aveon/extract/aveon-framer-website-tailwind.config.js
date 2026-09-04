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
            '50': 'hsl(26, 39%, 97%)',
            '100': 'hsl(26, 39%, 94%)',
            '200': 'hsl(26, 39%, 86%)',
            '300': 'hsl(26, 39%, 76%)',
            '400': 'hsl(26, 39%, 64%)',
            '500': 'hsl(26, 39%, 50%)',
            '600': 'hsl(26, 39%, 40%)',
            '700': 'hsl(26, 39%, 32%)',
            '800': 'hsl(26, 39%, 24%)',
            '900': 'hsl(26, 39%, 16%)',
            '950': 'hsl(26, 39%, 10%)',
            DEFAULT: '#b8845c'
        },
        accent: {
            '50': 'hsl(30, 29%, 97%)',
            '100': 'hsl(30, 29%, 94%)',
            '200': 'hsl(30, 29%, 86%)',
            '300': 'hsl(30, 29%, 76%)',
            '400': 'hsl(30, 29%, 64%)',
            '500': 'hsl(30, 29%, 50%)',
            '600': 'hsl(30, 29%, 40%)',
            '700': 'hsl(30, 29%, 32%)',
            '800': 'hsl(30, 29%, 24%)',
            '900': 'hsl(30, 29%, 16%)',
            '950': 'hsl(30, 29%, 10%)',
            DEFAULT: '#2c2218'
        },
        'neutral-50': '#000000',
        'neutral-100': '#1a1a1a',
        'neutral-200': '#e5ddd4',
        'neutral-300': '#ffffff',
        'neutral-400': '#767676',
        'neutral-500': '#3e3228',
        background: '#e8e0d6',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Geist',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ]
    },
    fontSize: {
        '11': [
            '11px',
            {
                lineHeight: '16.5px'
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
                lineHeight: '15.6px',
                letterSpacing: '-0.26px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '16.8px',
                letterSpacing: '-0.28px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '24.2px',
                letterSpacing: '-1.32px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '36px',
                letterSpacing: '-1.8px'
            }
        ],
        '44': [
            '44px',
            {
                lineHeight: '44px',
                letterSpacing: '-2.64px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '60px',
                letterSpacing: '-1.8px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '80px',
                letterSpacing: '-4.8px'
            }
        ],
        '144': [
            '144px',
            {
                lineHeight: '129.6px',
                letterSpacing: '-10.08px'
            }
        ]
    },
    spacing: {
        '20': '40px',
        '30': '60px',
        '33': '66px',
        '40': '80px',
        '50': '100px',
        '60': '120px',
        '120': '240px',
        '1px': '1px'
    },
    borderRadius: {
        sm: '5px',
        md: '10px',
        lg: '16px',
        xl: '20px',
        full: '999px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '250': '0.25s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1520px'
    }
},
  },
};

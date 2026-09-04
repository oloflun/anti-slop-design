/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(27, 100%, 97%)',
            '100': 'hsl(27, 100%, 94%)',
            '200': 'hsl(27, 100%, 86%)',
            '300': 'hsl(27, 100%, 76%)',
            '400': 'hsl(27, 100%, 64%)',
            '500': 'hsl(27, 100%, 50%)',
            '600': 'hsl(27, 100%, 40%)',
            '700': 'hsl(27, 100%, 32%)',
            '800': 'hsl(27, 100%, 24%)',
            '900': 'hsl(27, 100%, 16%)',
            '950': 'hsl(27, 100%, 10%)',
            DEFAULT: '#fffaf6'
        },
        secondary: {
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
        accent: {
            '50': 'hsl(50, 30%, 97%)',
            '100': 'hsl(50, 30%, 94%)',
            '200': 'hsl(50, 30%, 86%)',
            '300': 'hsl(50, 30%, 76%)',
            '400': 'hsl(50, 30%, 64%)',
            '500': 'hsl(50, 30%, 50%)',
            '600': 'hsl(50, 30%, 40%)',
            '700': 'hsl(50, 30%, 32%)',
            '800': 'hsl(50, 30%, 24%)',
            '900': 'hsl(50, 30%, 16%)',
            '950': 'hsl(50, 30%, 10%)',
            DEFAULT: '#f1efe5'
        },
        'neutral-50': '#000000',
        'neutral-100': '#100c08',
        'neutral-200': '#767676',
        background: '#100c08',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Times New Roman',
            'sans-serif'
        ],
        heading: [
            'Libre Caslon Condensed Variable',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: 'normal'
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
        '17': [
            '17px',
            {
                lineHeight: '22.1px',
                letterSpacing: '-0.34px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '23.4px',
                letterSpacing: '-0.36px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '43.2px'
            }
        ],
        '144': [
            '144px',
            {
                lineHeight: '158.4px'
            }
        ],
        '14.4': [
            '14.4px',
            {
                lineHeight: '18px'
            }
        ]
    },
    spacing: {
        '8': '32px',
        '12': '48px',
        '16': '64px',
        '20': '80px',
        '24': '96px',
        '28': '112px',
        '45': '180px',
        '1px': '1px'
    },
    borderRadius: {
        sm: '4px',
        md: '10px',
        lg: '16px',
        full: '100px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '810px',
        '910px': '910px'
    },
    transitionDuration: {
        '400': '0.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.075, 0.82, 0.165, 1)'
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

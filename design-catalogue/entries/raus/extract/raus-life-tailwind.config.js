/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(251, 14%, 97%)',
            '100': 'hsl(251, 14%, 94%)',
            '200': 'hsl(251, 14%, 86%)',
            '300': 'hsl(251, 14%, 76%)',
            '400': 'hsl(251, 14%, 64%)',
            '500': 'hsl(251, 14%, 50%)',
            '600': 'hsl(251, 14%, 40%)',
            '700': 'hsl(251, 14%, 32%)',
            '800': 'hsl(251, 14%, 24%)',
            '900': 'hsl(251, 14%, 16%)',
            '950': 'hsl(251, 14%, 10%)',
            DEFAULT: '#23212c'
        },
        secondary: {
            '50': 'hsl(22, 100%, 97%)',
            '100': 'hsl(22, 100%, 94%)',
            '200': 'hsl(22, 100%, 86%)',
            '300': 'hsl(22, 100%, 76%)',
            '400': 'hsl(22, 100%, 64%)',
            '500': 'hsl(22, 100%, 50%)',
            '600': 'hsl(22, 100%, 40%)',
            '700': 'hsl(22, 100%, 32%)',
            '800': 'hsl(22, 100%, 24%)',
            '900': 'hsl(22, 100%, 16%)',
            '950': 'hsl(22, 100%, 10%)',
            DEFAULT: '#dd5000'
        },
        accent: {
            '50': 'hsl(202, 100%, 97%)',
            '100': 'hsl(202, 100%, 94%)',
            '200': 'hsl(202, 100%, 86%)',
            '300': 'hsl(202, 100%, 76%)',
            '400': 'hsl(202, 100%, 64%)',
            '500': 'hsl(202, 100%, 50%)',
            '600': 'hsl(202, 100%, 40%)',
            '700': 'hsl(202, 100%, 32%)',
            '800': 'hsl(202, 100%, 24%)',
            '900': 'hsl(202, 100%, 16%)',
            '950': 'hsl(202, 100%, 10%)',
            DEFAULT: '#a6dfff'
        },
        'neutral-50': '#ffffff',
        'neutral-100': '#fdf9ed',
        'neutral-200': '#000000',
        background: '#fdf9ed',
        foreground: '#23212c'
    },
    fontFamily: {
        sans: [
            'neue-haas-unica',
            'sans-serif'
        ],
        heading: [
            'fonts',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '16px',
                letterSpacing: '-0.06px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18px',
                letterSpacing: '-0.14px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '18.4px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '22px',
                letterSpacing: '-0.18px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '26px',
                letterSpacing: '-0.22px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '30px',
                letterSpacing: '-0.42px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '36px',
                letterSpacing: '-0.54px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '38px',
                letterSpacing: '-0.8px'
            }
        ],
        '84': [
            '84px',
            {
                lineHeight: '76px',
                letterSpacing: '-2.52px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '16': '32px',
        '20': '40px',
        '24': '48px',
        '40': '80px',
        '48': '96px',
        '60': '120px',
        '96': '192px',
        '53px': '53px',
        '211px': '211px'
    },
    borderRadius: {
        sm: '4px',
        lg: '16px',
        xl: '20px',
        full: '99px'
    },
    screens: {
        sm: '576px',
        md: '768px',
        lg: '992px',
        '1200px': '1200px'
    },
    transitionDuration: {
        '100': '0.1s',
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.665, 0.425, 0.44, 1.105)'
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

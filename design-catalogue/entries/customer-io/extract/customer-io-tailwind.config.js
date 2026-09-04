/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
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
            DEFAULT: '#fff8e9'
        },
        secondary: {
            '50': 'hsl(192, 83%, 97%)',
            '100': 'hsl(192, 83%, 94%)',
            '200': 'hsl(192, 83%, 86%)',
            '300': 'hsl(192, 83%, 76%)',
            '400': 'hsl(192, 83%, 64%)',
            '500': 'hsl(192, 83%, 50%)',
            '600': 'hsl(192, 83%, 40%)',
            '700': 'hsl(192, 83%, 32%)',
            '800': 'hsl(192, 83%, 24%)',
            '900': 'hsl(192, 83%, 16%)',
            '950': 'hsl(192, 83%, 10%)',
            DEFAULT: '#01090b'
        },
        accent: {
            '50': 'hsl(204, 100%, 97%)',
            '100': 'hsl(204, 100%, 94%)',
            '200': 'hsl(204, 100%, 86%)',
            '300': 'hsl(204, 100%, 76%)',
            '400': 'hsl(204, 100%, 64%)',
            '500': 'hsl(204, 100%, 50%)',
            '600': 'hsl(204, 100%, 40%)',
            '700': 'hsl(204, 100%, 32%)',
            '800': 'hsl(204, 100%, 24%)',
            '900': 'hsl(204, 100%, 16%)',
            '950': 'hsl(204, 100%, 10%)',
            DEFAULT: '#c3e7ff'
        },
        'neutral-50': '#d4d4d4',
        'neutral-100': '#ffffff',
        'neutral-200': '#5a8990',
        'neutral-300': '#f4f4f4',
        background: '#000405',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'saansFont',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '13.75px',
                letterSpacing: '0.2px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '16.5px',
                letterSpacing: '0.2px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '19.25px',
                letterSpacing: '0.2px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '22px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '24.75px',
                letterSpacing: '0.2px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '27.5px',
                letterSpacing: '0.2px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '27px',
                letterSpacing: '0.2px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '33.75px',
                letterSpacing: '0.2px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '40.5px',
                letterSpacing: '0.2px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '45px',
                letterSpacing: '0.2px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '64px',
                letterSpacing: '0.2px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '96px',
                letterSpacing: '0.2px'
            }
        ]
    },
    spacing: {
        '10': '40px',
        '12': '48px',
        '16': '64px',
        '20': '80px',
        '24': '96px',
        '30': '120px',
        '32': '128px',
        '40': '160px',
        '1px': '1px'
    },
    borderRadius: {
        xs: '2px',
        md: '6px'
    },
    boxShadow: {
        sm: 'oklch(0.97 0 0) 0px 0px 0px 4px'
    },
    transitionDuration: {
        '200': '0.2s',
        '400': '0.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0, 0, 0.2, 1)'
    },
    container: {
        center: true,
        padding: '32px'
    },
    maxWidth: {
        container: '1320px'
    }
},
  },
};

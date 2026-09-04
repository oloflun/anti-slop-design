/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(68, 100%, 97%)',
            '100': 'hsl(68, 100%, 94%)',
            '200': 'hsl(68, 100%, 86%)',
            '300': 'hsl(68, 100%, 76%)',
            '400': 'hsl(68, 100%, 64%)',
            '500': 'hsl(68, 100%, 50%)',
            '600': 'hsl(68, 100%, 40%)',
            '700': 'hsl(68, 100%, 32%)',
            '800': 'hsl(68, 100%, 24%)',
            '900': 'hsl(68, 100%, 16%)',
            '950': 'hsl(68, 100%, 10%)',
            DEFAULT: '#eaff62'
        },
        secondary: {
            '50': 'hsl(136, 36%, 97%)',
            '100': 'hsl(136, 36%, 94%)',
            '200': 'hsl(136, 36%, 86%)',
            '300': 'hsl(136, 36%, 76%)',
            '400': 'hsl(136, 36%, 64%)',
            '500': 'hsl(136, 36%, 50%)',
            '600': 'hsl(136, 36%, 40%)',
            '700': 'hsl(136, 36%, 32%)',
            '800': 'hsl(136, 36%, 24%)',
            '900': 'hsl(136, 36%, 16%)',
            '950': 'hsl(136, 36%, 10%)',
            DEFAULT: '#377648'
        },
        'neutral-50': '#000000',
        background: '#377648',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Annuario',
            'sans-serif'
        ],
        body: [
            'Tuppence',
            'sans-serif'
        ]
    },
    fontSize: {
        '11': [
            '11px',
            {
                lineHeight: '11px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '14px',
                letterSpacing: '0.25px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '16px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '18px',
                letterSpacing: '1.8px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '96': '192px',
        '136': '272px',
        '483px': '483px'
    },
    screens: {
        sm: '601px'
    },
    transitionDuration: {
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.56, 0.56, 0.4, 1.13)'
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

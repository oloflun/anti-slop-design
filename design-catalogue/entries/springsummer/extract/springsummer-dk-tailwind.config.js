/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(0, 99%, 97%)',
            '100': 'hsl(0, 99%, 94%)',
            '200': 'hsl(0, 99%, 86%)',
            '300': 'hsl(0, 99%, 76%)',
            '400': 'hsl(0, 99%, 64%)',
            '500': 'hsl(0, 99%, 50%)',
            '600': 'hsl(0, 99%, 40%)',
            '700': 'hsl(0, 99%, 32%)',
            '800': 'hsl(0, 99%, 24%)',
            '900': 'hsl(0, 99%, 16%)',
            '950': 'hsl(0, 99%, 10%)',
            DEFAULT: '#fe3939'
        },
        'neutral-50': '#ffffff',
        'neutral-100': '#000000',
        'neutral-200': '#dedcd3',
        background: '#dedcd3',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Montreal',
            'sans-serif'
        ],
        heading: [
            'Supply',
            'sans-serif'
        ],
        font2: [
            'Grotesk',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '12.6px',
                letterSpacing: '0.1px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '15.6px',
                letterSpacing: '0.276px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '21px',
                letterSpacing: '0.28px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '25.2px',
                letterSpacing: '0.36px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: 'normal'
            }
        ],
        '25': [
            '25px',
            {
                lineHeight: '35px',
                letterSpacing: '0.5px'
            }
        ],
        '331.84': [
            '331.84px',
            {
                lineHeight: '248.946px'
            }
        ],
        '146.4': [
            '146.4px',
            {
                lineHeight: '111.264px'
            }
        ],
        '38.4': [
            '38.4px',
            {
                lineHeight: '42.24px',
                letterSpacing: '0.768px'
            }
        ],
        '13.3333': [
            '13.3333px',
            {
                lineHeight: 'normal'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '9': '18px',
        '15': '30px',
        '20': '40px',
        '25': '50px',
        '30': '60px',
        '40': '80px',
        '50': '100px',
        '75': '150px',
        '125': '250px'
    },
    borderRadius: {
        sm: '3px',
        full: '50px'
    },
    screens: {
        '900px': '900px',
        '1200px': '1200px'
    },
    transitionDuration: {
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s',
        '800': '0.8s',
        '1000': '1s',
        '1300': '1.3s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0, 0.55, 0.45, 1)'
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

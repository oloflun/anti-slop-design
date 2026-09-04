/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(30, 24%, 97%)',
            '100': 'hsl(30, 24%, 94%)',
            '200': 'hsl(30, 24%, 86%)',
            '300': 'hsl(30, 24%, 76%)',
            '400': 'hsl(30, 24%, 64%)',
            '500': 'hsl(30, 24%, 50%)',
            '600': 'hsl(30, 24%, 40%)',
            '700': 'hsl(30, 24%, 32%)',
            '800': 'hsl(30, 24%, 24%)',
            '900': 'hsl(30, 24%, 16%)',
            '950': 'hsl(30, 24%, 10%)',
            DEFAULT: '#f2eeea'
        },
        'neutral-50': '#867c73',
        'neutral-100': '#000000',
        'neutral-200': '#34312e',
        'neutral-300': '#6c645c',
        'neutral-400': '#5e5853',
        'neutral-500': '#474340',
        'neutral-600': '#ffffff',
        background: '#867c73',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Monument Grotesk',
            'sans-serif'
        ],
        body: [
            'GT Super Text',
            'sans-serif'
        ]
    },
    fontSize: {
        '11': [
            '11px',
            {
                lineHeight: 'normal',
                letterSpacing: '0.66px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: 'normal',
                letterSpacing: '0.72px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: 'normal',
                letterSpacing: '0.15px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: 'normal',
                letterSpacing: '0.15px'
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
                lineHeight: '18px',
                letterSpacing: '1.08px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: 'normal',
                letterSpacing: '-0.24px'
            }
        ],
        '33': [
            '33px',
            {
                lineHeight: '33px',
                letterSpacing: '-0.99px'
            }
        ],
        '65': [
            '65px',
            {
                lineHeight: '55.25px',
                letterSpacing: '-0.65px'
            }
        ]
    },
    spacing: {
        '2': '4px',
        '15': '30px',
        '20': '40px',
        '54': '108px',
        '73': '146px',
        '136': '272px',
        '154': '308px',
        '79px': '79px',
        '225px': '225px',
        '427px': '427px'
    },
    borderRadius: {
        xs: '1px',
        sm: '5px',
        md: '10px',
        full: '1280px'
    },
    transitionDuration: {
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '500': '0.5s',
        '650': '0.65s',
        '850': '0.85s',
        '1000': '1s',
        '1200': '1.2s',
        '1250': '1.25s'
    },
    transitionTimingFunction: {
        default: 'ease',
        linear: 'linear'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1800px'
    }
},
  },
};

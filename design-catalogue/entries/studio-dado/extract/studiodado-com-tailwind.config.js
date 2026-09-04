/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#1b1b1c',
        'neutral-300': '#5d5346',
        background: '#5d5346',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'sans',
            'sans-serif'
        ],
        heading: [
            'disp',
            'sans-serif'
        ]
    },
    fontSize: {
        '187.733': [
            '187.733px',
            {
                lineHeight: '150.187px',
                letterSpacing: '-3.75467px'
            }
        ],
        '138.24': [
            '138.24px',
            {
                lineHeight: '110.592px',
                letterSpacing: '-2.7648px'
            }
        ],
        '59.7333': [
            '59.7333px',
            {
                lineHeight: '60.928px',
                letterSpacing: '-1.19467px'
            }
        ],
        '34.1333': [
            '34.1333px',
            {
                lineHeight: '40.96px',
                letterSpacing: '-0.341333px'
            }
        ],
        '25.6': [
            '25.6px',
            {
                lineHeight: '28.16px',
                letterSpacing: '-0.341333px'
            }
        ],
        '17.0667': [
            '17.0667px',
            {
                lineHeight: '20.48px',
                letterSpacing: '-0.341333px'
            }
        ],
        '11.9467': [
            '11.9467px',
            {
                lineHeight: '14.336px',
                letterSpacing: '-0.341333px'
            }
        ],
        '8.53333': [
            '8.53333px',
            {
                lineHeight: '10.24px'
            }
        ]
    },
    spacing: {
        '60': '120px',
        '77': '154px',
        '104': '208px',
        '141': '282px',
        '158': '316px',
        '197': '394px',
        '222': '444px',
        '9px': '9px',
        '85px': '85px',
        '239px': '239px'
    },
    borderRadius: {
        full: '9999px'
    },
    screens: {
        sm: '650px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '1440px': '1440px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '500': '0.5s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.23, 1, 0.32, 1)',
        default: 'ease'
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

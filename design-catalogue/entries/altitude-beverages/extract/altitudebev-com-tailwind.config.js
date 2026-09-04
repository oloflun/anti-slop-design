/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#fafafa',
        'neutral-100': '#000000',
        'neutral-200': '#53606e',
        'neutral-300': '#808080',
        background: '#808080',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'DepartureMono',
            'sans-serif'
        ],
        body: [
            'HelveticaNowDisplay',
            'sans-serif'
        ],
        font2: [
            'EditorialNew',
            'sans-serif'
        ]
    },
    fontSize: {
        '11': [
            '11px',
            {
                lineHeight: '11px',
                letterSpacing: '-0.55px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '28px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '20px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '16.2px',
                letterSpacing: '-0.9px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '42.4px',
                letterSpacing: '-1px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '63.6px',
                letterSpacing: '-1.5px'
            }
        ],
        '160': [
            '160px',
            {
                lineHeight: '160px',
                letterSpacing: '-8px'
            }
        ],
        '11.2': [
            '11.2px',
            {
                lineHeight: '20px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '18': '36px',
        '24': '48px',
        '28': '56px',
        '32': '64px',
        '39': '78px',
        '48': '96px',
        '144': '288px',
        '160': '320px',
        '85px': '85px',
        '125px': '125px',
        '265px': '265px',
        '333px': '333px',
        '495px': '495px'
    },
    borderRadius: {
        full: '110px'
    },
    transitionDuration: {
        '150': '0.15s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.4, 0, 0.2, 1)'
    },
    container: {
        center: true,
        padding: '48px'
    },
    maxWidth: {
        container: '1024px'
    }
},
  },
};

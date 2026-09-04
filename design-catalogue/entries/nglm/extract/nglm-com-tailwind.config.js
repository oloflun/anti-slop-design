/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#000000',
        'neutral-100': '#51585c',
        'neutral-200': '#fcfcfc',
        'neutral-300': '#c0c3c3',
        'neutral-400': '#707575',
        'neutral-500': '#131516',
        background: '#fcfcfc',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'GD Gaio VF',
            'sans-serif'
        ],
        heading: [
            'GD Trio Display',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '13.44px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '16.24px'
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
                lineHeight: '21.6px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '30.8px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '53.76px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '76.8px'
            }
        ],
        '140.8': [
            '140.8px',
            {
                lineHeight: '140.8px'
            }
        ],
        '102.4': [
            '102.4px',
            {
                lineHeight: '102.4px'
            }
        ],
        '83.2': [
            '83.2px',
            {
                lineHeight: '73.216px',
                letterSpacing: '-0.832px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '32': '64px',
        '40': '80px',
        '52': '104px',
        '88': '176px',
        '172': '344px'
    },
    borderRadius: {
        xs: '2px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0.2) 0px 0px 4px 0px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '300': '0.3s',
        '400': '0.4s',
        '450': '0.45s',
        '500': '0.5s',
        '550': '0.55s',
        '600': '0.6s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.77, 0, 0.175, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1280px'
    }
},
  },
};

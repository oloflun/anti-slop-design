/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#292a2c',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        'neutral-300': '#999999',
        'neutral-400': '#f2f2f2',
        'neutral-500': '#cccccc',
        background: '#f2f2f2',
        foreground: '#292a2c'
    },
    fontFamily: {
        sans: [
            'telegraf',
            'sans-serif'
        ],
        body: [
            'Arial',
            'sans-serif'
        ]
    },
    fontSize: {
        '0': [
            '0px',
            {
                lineHeight: '0px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '61.9999px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '30.0001px',
                letterSpacing: '0.5px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '30.0001px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '0px',
                letterSpacing: '0.5px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '22px'
            }
        ],
        '25': [
            '25px',
            {
                lineHeight: '25px',
                letterSpacing: '1px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '46.6668px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '32px'
            }
        ],
        '38': [
            '38px',
            {
                lineHeight: '41.8px',
                letterSpacing: '0.1px'
            }
        ],
        '25.5': [
            '25.5px',
            {
                lineHeight: '38.25px',
                letterSpacing: '-0.5px'
            }
        ],
        '23.94': [
            '23.94px',
            {
                lineHeight: '35.91px',
                letterSpacing: '0.5px'
            }
        ],
        '18.5395': [
            '18.5395px',
            {
                lineHeight: '22.2474px',
                letterSpacing: '-0.5px'
            }
        ],
        '18.176': [
            '18.176px',
            {
                lineHeight: '21.8112px',
                letterSpacing: '0.5px'
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
        '15': '30px',
        '20': '40px',
        '40': '80px',
        '50': '100px',
        '55': '110px',
        '75': '150px',
        '150': '300px',
        '200': '400px',
        '205': '410px',
        '1px': '1px',
        '63px': '63px'
    },
    borderRadius: {
        xs: '2px',
        full: '50px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0.25) 0px 1.99998px 5.00004px 0px'
    },
    screens: {
        md: '769px',
        lg: '993px',
        '1169px': '1169px',
        '1200px': '1200px',
        '1201px': '1201px',
        xl: '1300px',
        '1367px': '1367px',
        '1640px': '1640px',
        '2540px': '2540px',
        '2600px': '2600px'
    },
    transitionDuration: {
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '310': '0.31s',
        '333': '0.333s'
    },
    transitionTimingFunction: {
        linear: 'linear',
        custom: 'cubic-bezier(0.4, 0, 0.22, 1)',
        default: 'ease'
    },
    container: {
        center: true,
        padding: '43.9999px'
    },
    maxWidth: {
        container: '2648px'
    }
},
  },
};

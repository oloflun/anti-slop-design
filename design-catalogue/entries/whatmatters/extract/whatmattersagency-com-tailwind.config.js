/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(54, 99%, 97%)',
            '100': 'hsl(54, 99%, 94%)',
            '200': 'hsl(54, 99%, 86%)',
            '300': 'hsl(54, 99%, 76%)',
            '400': 'hsl(54, 99%, 64%)',
            '500': 'hsl(54, 99%, 50%)',
            '600': 'hsl(54, 99%, 40%)',
            '700': 'hsl(54, 99%, 32%)',
            '800': 'hsl(54, 99%, 24%)',
            '900': 'hsl(54, 99%, 16%)',
            '950': 'hsl(54, 99%, 10%)',
            DEFAULT: '#fef073'
        },
        secondary: {
            '50': 'hsl(31, 100%, 97%)',
            '100': 'hsl(31, 100%, 94%)',
            '200': 'hsl(31, 100%, 86%)',
            '300': 'hsl(31, 100%, 76%)',
            '400': 'hsl(31, 100%, 64%)',
            '500': 'hsl(31, 100%, 50%)',
            '600': 'hsl(31, 100%, 40%)',
            '700': 'hsl(31, 100%, 32%)',
            '800': 'hsl(31, 100%, 24%)',
            '900': 'hsl(31, 100%, 16%)',
            '950': 'hsl(31, 100%, 10%)',
            DEFAULT: '#ffa23c'
        },
        accent: {
            '50': 'hsl(216, 75%, 97%)',
            '100': 'hsl(216, 75%, 94%)',
            '200': 'hsl(216, 75%, 86%)',
            '300': 'hsl(216, 75%, 76%)',
            '400': 'hsl(216, 75%, 64%)',
            '500': 'hsl(216, 75%, 50%)',
            '600': 'hsl(216, 75%, 40%)',
            '700': 'hsl(216, 75%, 32%)',
            '800': 'hsl(216, 75%, 24%)',
            '900': 'hsl(216, 75%, 16%)',
            '950': 'hsl(216, 75%, 10%)',
            DEFAULT: '#5a92e7'
        },
        'neutral-50': '#050505',
        'neutral-100': '#ffffff',
        'neutral-200': '#6c6b6a',
        'neutral-300': '#312821',
        'neutral-400': '#f7f7f1',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Inter',
            'sans-serif'
        ],
        heading: [
            'Neue Haas Display',
            'sans-serif'
        ],
        font2: [
            'Denim Ink',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '32.4px',
                letterSpacing: '-0.157152px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '30px',
                letterSpacing: '-0.3px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '42px',
                letterSpacing: '-1px'
            }
        ],
        '98': [
            '98px',
            {
                lineHeight: '80.36px',
                letterSpacing: '-1.96px'
            }
        ],
        '135.434': [
            '135.434px',
            {
                lineHeight: '111.056px',
                letterSpacing: '-2.70867px'
            }
        ],
        '97.7152': [
            '97.7152px',
            {
                lineHeight: '97.7152px',
                letterSpacing: '-0.157152px'
            }
        ],
        '71.4336': [
            '71.4336px',
            {
                lineHeight: '58.5756px',
                letterSpacing: '-0.714336px'
            }
        ],
        '57.2768': [
            '57.2768px',
            {
                lineHeight: '57.2768px',
                letterSpacing: '-0.572768px'
            }
        ],
        '23.1488': [
            '23.1488px',
            {
                lineHeight: '25.4637px'
            }
        ],
        '20.5728': [
            '20.5728px',
            {
                lineHeight: '20.5728px',
                letterSpacing: '-0.205728px'
            }
        ],
        '19.7152': [
            '19.7152px',
            {
                lineHeight: '26.6155px',
                letterSpacing: '-0.157152px'
            }
        ],
        '17.7152': [
            '17.7152px',
            {
                lineHeight: '17.7152px',
                letterSpacing: '-0.177152px'
            }
        ],
        '15.7152': [
            '15.7152px',
            {
                lineHeight: '21.2155px',
                letterSpacing: '-0.157152px'
            }
        ],
        '15.1424': [
            '15.1424px',
            {
                lineHeight: '20.4422px',
                letterSpacing: '-0.157152px'
            }
        ]
    },
    spacing: {
        '0': '2px',
        '1': '12px',
        '2': '14px',
        '3': '24px',
        '4': '27px',
        '5': '31px',
        '6': '35px',
        '7': '39px',
        '8': '63px',
        '9': '67px',
        '10': '70px',
        '11': '72px',
        '12': '75px',
        '13': '93px',
        '14': '122px',
        '15': '180px',
        '16': '370px'
    },
    borderRadius: {
        xs: '2px',
        full: '800px'
    },
    boxShadow: {
        sm: 'rgb(5, 5, 5) 0px 3.6808px 0px 0px'
    },
    transitionDuration: {
        '20': '0.02s',
        '40': '0.04s',
        '60': '0.06s',
        '80': '0.08s',
        '100': '0.1s',
        '120': '0.12s',
        '140': '0.14s',
        '150': '0.15s',
        '160': '0.16s',
        '180': '0.18s',
        '200': '0.2s',
        '220': '0.22s',
        '240': '0.24s',
        '250': '0.25s',
        '260': '0.26s',
        '280': '0.28s',
        '300': '0.3s',
        '320': '0.32s',
        '340': '0.34s',
        '360': '0.36s',
        '380': '0.38s',
        '400': '0.4s',
        '420': '0.42s',
        '440': '0.44s',
        '500': '0.5s',
        '600': '0.6s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.625, 0.5, 0, 1)',
        default: 'ease',
        linear: 'linear'
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

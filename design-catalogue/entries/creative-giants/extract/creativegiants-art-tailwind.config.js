/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(53, 100%, 97%)',
            '100': 'hsl(53, 100%, 94%)',
            '200': 'hsl(53, 100%, 86%)',
            '300': 'hsl(53, 100%, 76%)',
            '400': 'hsl(53, 100%, 64%)',
            '500': 'hsl(53, 100%, 50%)',
            '600': 'hsl(53, 100%, 40%)',
            '700': 'hsl(53, 100%, 32%)',
            '800': 'hsl(53, 100%, 24%)',
            '900': 'hsl(53, 100%, 16%)',
            '950': 'hsl(53, 100%, 10%)',
            DEFAULT: '#fffef7'
        },
        secondary: {
            '50': 'hsl(203, 100%, 97%)',
            '100': 'hsl(203, 100%, 94%)',
            '200': 'hsl(203, 100%, 86%)',
            '300': 'hsl(203, 100%, 76%)',
            '400': 'hsl(203, 100%, 64%)',
            '500': 'hsl(203, 100%, 50%)',
            '600': 'hsl(203, 100%, 40%)',
            '700': 'hsl(203, 100%, 32%)',
            '800': 'hsl(203, 100%, 24%)',
            '900': 'hsl(203, 100%, 16%)',
            '950': 'hsl(203, 100%, 10%)',
            DEFAULT: '#009fff'
        },
        accent: {
            '50': 'hsl(49, 100%, 97%)',
            '100': 'hsl(49, 100%, 94%)',
            '200': 'hsl(49, 100%, 86%)',
            '300': 'hsl(49, 100%, 76%)',
            '400': 'hsl(49, 100%, 64%)',
            '500': 'hsl(49, 100%, 50%)',
            '600': 'hsl(49, 100%, 40%)',
            '700': 'hsl(49, 100%, 32%)',
            '800': 'hsl(49, 100%, 24%)',
            '900': 'hsl(49, 100%, 16%)',
            '950': 'hsl(49, 100%, 10%)',
            DEFAULT: '#ffd001'
        },
        'neutral-50': '#000000',
        'neutral-100': '#efeeec',
        'neutral-200': '#666666',
        'neutral-300': '#aaaaaa',
        'neutral-400': '#1f1f1f',
        'neutral-500': '#131313',
        'neutral-600': '#444444',
        'neutral-700': '#cccccc',
        'neutral-800': '#dddddd',
        'neutral-900': '#ecfdf3',
        background: '#fffef7',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Switzer',
            'sans-serif'
        ]
    },
    fontSize: {
        '80.2584': [
            '80.2584px',
            {
                lineHeight: '60.1938px',
                letterSpacing: '-3.21033px'
            }
        ],
        '61.1492': [
            '61.1492px',
            {
                lineHeight: '61.1492px',
                letterSpacing: '-2.44597px'
            }
        ],
        '51.5947': [
            '51.5947px',
            {
                lineHeight: '51.5947px',
                letterSpacing: '-2.06379px'
            }
        ],
        '32.4855': [
            '32.4855px',
            {
                lineHeight: '32.4855px',
                letterSpacing: '-1.29942px'
            }
        ],
        '19.1091': [
            '19.1091px',
            {
                lineHeight: '26.7528px',
                letterSpacing: '-0.764365px'
            }
        ],
        '17.1982': [
            '17.1982px',
            {
                lineHeight: '17.1982px'
            }
        ],
        '15.2873': [
            '15.2873px',
            {
                lineHeight: 'normal'
            }
        ],
        '13.3764': [
            '13.3764px',
            {
                lineHeight: '18.7269px',
                letterSpacing: '-0.305746px'
            }
        ],
        '11.4655': [
            '11.4655px',
            {
                lineHeight: '16.0517px',
                letterSpacing: '-0.305746px'
            }
        ]
    },
    spacing: {
        '0': '1px',
        '1': '31px',
        '2': '38px',
        '3': '46px',
        '4': '61px',
        '5': '76px',
        '6': '107px',
        '7': '117px',
        '8': '153px',
        '9': '173px',
        '10': '190px',
        '11': '232px',
        '12': '255px',
        '13': '313px',
        '14': '387px',
        '15': '400px'
    },
    borderRadius: {
        xl: '23px',
        full: '1529px'
    },
    boxShadow: {
        sm: 'rgba(255, 255, 255, 0.2) 0px 0px 0px 1px'
    },
    screens: {
        md: '768px',
        lg: '991px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s',
        '375': '0.375s',
        '550': '0.55s',
        '600': '0.6s',
        '700': '0.7s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.25, 0.1, 0.25, 1)',
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

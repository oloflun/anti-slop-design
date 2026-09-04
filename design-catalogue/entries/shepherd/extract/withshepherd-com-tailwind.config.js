/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(43, 98%, 97%)',
            '100': 'hsl(43, 98%, 94%)',
            '200': 'hsl(43, 98%, 86%)',
            '300': 'hsl(43, 98%, 76%)',
            '400': 'hsl(43, 98%, 64%)',
            '500': 'hsl(43, 98%, 50%)',
            '600': 'hsl(43, 98%, 40%)',
            '700': 'hsl(43, 98%, 32%)',
            '800': 'hsl(43, 98%, 24%)',
            '900': 'hsl(43, 98%, 16%)',
            '950': 'hsl(43, 98%, 10%)',
            DEFAULT: '#fdc331'
        },
        secondary: {
            '50': 'hsl(29, 29%, 97%)',
            '100': 'hsl(29, 29%, 94%)',
            '200': 'hsl(29, 29%, 86%)',
            '300': 'hsl(29, 29%, 76%)',
            '400': 'hsl(29, 29%, 64%)',
            '500': 'hsl(29, 29%, 50%)',
            '600': 'hsl(29, 29%, 40%)',
            '700': 'hsl(29, 29%, 32%)',
            '800': 'hsl(29, 29%, 24%)',
            '900': 'hsl(29, 29%, 16%)',
            '950': 'hsl(29, 29%, 10%)',
            DEFAULT: '#d6c5b5'
        },
        accent: {
            '50': 'hsl(28, 95%, 97%)',
            '100': 'hsl(28, 95%, 94%)',
            '200': 'hsl(28, 95%, 86%)',
            '300': 'hsl(28, 95%, 76%)',
            '400': 'hsl(28, 95%, 64%)',
            '500': 'hsl(28, 95%, 50%)',
            '600': 'hsl(28, 95%, 40%)',
            '700': 'hsl(28, 95%, 32%)',
            '800': 'hsl(28, 95%, 24%)',
            '900': 'hsl(28, 95%, 16%)',
            '950': 'hsl(28, 95%, 10%)',
            DEFAULT: '#fa9742'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#e7e7e7',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Magistersttrial',
            'sans-serif'
        ],
        heading: [
            'Gt Planar Trial',
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
                lineHeight: '26.4px',
                letterSpacing: '-0.714px'
            }
        ],
        '45': [
            '45px',
            {
                lineHeight: '45px',
                letterSpacing: '-2.25px'
            }
        ],
        '85': [
            '85px',
            {
                lineHeight: '85px',
                letterSpacing: '-4.25px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '100px',
                letterSpacing: '-3px'
            }
        ],
        '23.8': [
            '23.8px',
            {
                lineHeight: '26.18px',
                letterSpacing: '-0.714px'
            }
        ],
        '18.4': [
            '18.4px',
            {
                lineHeight: '20.24px',
                letterSpacing: '0.552px'
            }
        ],
        '15.5': [
            '15.5px',
            {
                lineHeight: '17.05px',
                letterSpacing: '0.775px'
            }
        ]
    },
    spacing: {
        '0': '2px',
        '1': '40px',
        '2': '53px',
        '3': '58px',
        '4': '69px',
        '5': '79px',
        '6': '84px',
        '7': '92px',
        '8': '115px',
        '9': '126px',
        '10': '208px',
        '11': '409px'
    },
    borderRadius: {
        md: '8px'
    },
    screens: {
        sm: '576px',
        md: '768px',
        lg: '992px',
        '1200px': '1200px',
        '1408px': '1408px',
        '1632px': '1632px'
    },
    transitionDuration: {
        '100': '0.1s',
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '600': '0.6s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1600px'
    }
},
  },
};

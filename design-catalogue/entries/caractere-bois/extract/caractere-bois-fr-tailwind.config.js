/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(9, 91%, 97%)',
            '100': 'hsl(9, 91%, 94%)',
            '200': 'hsl(9, 91%, 86%)',
            '300': 'hsl(9, 91%, 76%)',
            '400': 'hsl(9, 91%, 64%)',
            '500': 'hsl(9, 91%, 50%)',
            '600': 'hsl(9, 91%, 40%)',
            '700': 'hsl(9, 91%, 32%)',
            '800': 'hsl(9, 91%, 24%)',
            '900': 'hsl(9, 91%, 16%)',
            '950': 'hsl(9, 91%, 10%)',
            DEFAULT: '#f4300f'
        },
        secondary: {
            '50': 'hsl(240, 100%, 97%)',
            '100': 'hsl(240, 100%, 94%)',
            '200': 'hsl(240, 100%, 86%)',
            '300': 'hsl(240, 100%, 76%)',
            '400': 'hsl(240, 100%, 64%)',
            '500': 'hsl(240, 100%, 50%)',
            '600': 'hsl(240, 100%, 40%)',
            '700': 'hsl(240, 100%, 32%)',
            '800': 'hsl(240, 100%, 24%)',
            '900': 'hsl(240, 100%, 16%)',
            '950': 'hsl(240, 100%, 10%)',
            DEFAULT: '#0000ee'
        },
        accent: {
            '50': 'hsl(216, 100%, 97%)',
            '100': 'hsl(216, 100%, 94%)',
            '200': 'hsl(216, 100%, 86%)',
            '300': 'hsl(216, 100%, 76%)',
            '400': 'hsl(216, 100%, 64%)',
            '500': 'hsl(216, 100%, 50%)',
            '600': 'hsl(216, 100%, 40%)',
            '700': 'hsl(216, 100%, 32%)',
            '800': 'hsl(216, 100%, 24%)',
            '900': 'hsl(216, 100%, 16%)',
            '950': 'hsl(216, 100%, 10%)',
            DEFAULT: '#9cc4ff'
        },
        'neutral-50': '#333333',
        'neutral-100': '#eaeaea',
        'neutral-200': '#000000',
        'neutral-300': '#ffffff',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Arial',
            'sans-serif'
        ],
        heading: [
            'PP Migra',
            'sans-serif'
        ],
        font2: [
            'studiofeixensans',
            'sans-serif'
        ],
        body: [
            'PP migra',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: '20px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '40px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '92px'
            }
        ],
        '136': [
            '136px',
            {
                lineHeight: '125.12px'
            }
        ],
        '51.2': [
            '51.2px',
            {
                lineHeight: '47.104px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '20': '40px',
        '24': '48px',
        '29': '58px',
        '41': '82px',
        '185': '370px',
        '239': '478px'
    },
    borderRadius: {
        md: '8px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '200': '0.2s',
        '400': '0.4s',
        '1000': '1s'
    },
    transitionTimingFunction: {
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

/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(43, 14%, 97%)',
            '100': 'hsl(43, 14%, 94%)',
            '200': 'hsl(43, 14%, 86%)',
            '300': 'hsl(43, 14%, 76%)',
            '400': 'hsl(43, 14%, 64%)',
            '500': 'hsl(43, 14%, 50%)',
            '600': 'hsl(43, 14%, 40%)',
            '700': 'hsl(43, 14%, 32%)',
            '800': 'hsl(43, 14%, 24%)',
            '900': 'hsl(43, 14%, 16%)',
            '950': 'hsl(43, 14%, 10%)',
            DEFAULT: '#1c1a15'
        },
        secondary: {
            '50': 'hsl(48, 38%, 97%)',
            '100': 'hsl(48, 38%, 94%)',
            '200': 'hsl(48, 38%, 86%)',
            '300': 'hsl(48, 38%, 76%)',
            '400': 'hsl(48, 38%, 64%)',
            '500': 'hsl(48, 38%, 50%)',
            '600': 'hsl(48, 38%, 40%)',
            '700': 'hsl(48, 38%, 32%)',
            '800': 'hsl(48, 38%, 24%)',
            '900': 'hsl(48, 38%, 16%)',
            '950': 'hsl(48, 38%, 10%)',
            DEFAULT: '#fbfaf6'
        },
        accent: {
            '50': 'hsl(220, 100%, 97%)',
            '100': 'hsl(220, 100%, 94%)',
            '200': 'hsl(220, 100%, 86%)',
            '300': 'hsl(220, 100%, 76%)',
            '400': 'hsl(220, 100%, 64%)',
            '500': 'hsl(220, 100%, 50%)',
            '600': 'hsl(220, 100%, 40%)',
            '700': 'hsl(220, 100%, 32%)',
            '800': 'hsl(220, 100%, 24%)',
            '900': 'hsl(220, 100%, 16%)',
            '950': 'hsl(220, 100%, 10%)',
            DEFAULT: '#0055ff'
        },
        'neutral-50': '#000000',
        'neutral-100': '#56524a',
        'neutral-200': '#ece9e0',
        'neutral-300': '#8c887e',
        background: '#fbfaf6',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Onest',
            'sans-serif'
        ],
        heading: [
            'Sentient',
            'sans-serif'
        ],
        font2: [
            'Inter',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: 'normal'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '21px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '19.5px'
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
                lineHeight: '25.2px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '26px',
                letterSpacing: '-0.4px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '36.4px',
                letterSpacing: '-0.56px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '37.5px',
                letterSpacing: '-1.5px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '46px',
                letterSpacing: '-2px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '50.4px',
                letterSpacing: '-2.4px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '58.8px',
                letterSpacing: '-2.8px'
            }
        ]
    },
    spacing: {
        '4': '16px',
        '5': '20px',
        '7': '28px',
        '8': '32px',
        '10': '40px',
        '12': '48px',
        '15': '60px',
        '16': '64px',
        '18': '72px',
        '24': '96px',
        '1px': '1px'
    },
    borderRadius: {
        sm: '3px',
        md: '10px',
        lg: '16px',
        full: '50px'
    },
    boxShadow: {
        sm: 'rgba(0, 85, 255, 0.1) 0px 1px 3px 0px, rgba(0, 85, 255, 0.14) 0px 4px 16px 0px',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '810px'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1200px'
    }
},
  },
};

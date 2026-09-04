/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(360, 98%, 97%)',
            '100': 'hsl(360, 98%, 94%)',
            '200': 'hsl(360, 98%, 86%)',
            '300': 'hsl(360, 98%, 76%)',
            '400': 'hsl(360, 98%, 64%)',
            '500': 'hsl(360, 98%, 50%)',
            '600': 'hsl(360, 98%, 40%)',
            '700': 'hsl(360, 98%, 32%)',
            '800': 'hsl(360, 98%, 24%)',
            '900': 'hsl(360, 98%, 16%)',
            '950': 'hsl(360, 98%, 10%)',
            DEFAULT: '#df0203'
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
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#646464',
        'neutral-300': '#767676',
        'neutral-400': '#3d3d3d',
        'neutral-500': '#d6d6d6',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter Display',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ],
        font3: [
            'Open Sauce One',
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
                lineHeight: '21px',
                letterSpacing: '-0.28px'
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
                lineHeight: '21.6px',
                letterSpacing: '0.72px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '30px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '33.6px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '36.4px',
                letterSpacing: '-1.68px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '44.8px',
                letterSpacing: '-1.28px'
            }
        ],
        '42': [
            '42px',
            {
                lineHeight: 'normal'
            }
        ],
        '180': [
            '180px',
            {
                lineHeight: '162px',
                letterSpacing: '-12.6px'
            }
        ],
        '178.579': [
            '178.579px',
            {
                lineHeight: '160.721px',
                letterSpacing: '-10.7148px'
            }
        ]
    },
    spacing: {
        '10': '20px',
        '16': '32px',
        '27': '54px',
        '32': '64px',
        '40': '80px',
        '50': '100px',
        '65': '130px',
        '100': '200px',
        '1px': '1px'
    },
    borderRadius: {
        md: '10px',
        lg: '16px',
        full: '999px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '768px'
    },
    container: {
        center: true,
        padding: '25px'
    },
    maxWidth: {
        container: '1240px'
    }
},
  },
};

/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(28, 46%, 97%)',
            '100': 'hsl(28, 46%, 94%)',
            '200': 'hsl(28, 46%, 86%)',
            '300': 'hsl(28, 46%, 76%)',
            '400': 'hsl(28, 46%, 64%)',
            '500': 'hsl(28, 46%, 50%)',
            '600': 'hsl(28, 46%, 40%)',
            '700': 'hsl(28, 46%, 32%)',
            '800': 'hsl(28, 46%, 24%)',
            '900': 'hsl(28, 46%, 16%)',
            '950': 'hsl(28, 46%, 10%)',
            DEFAULT: '#392615'
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
            '50': 'hsl(30, 14%, 97%)',
            '100': 'hsl(30, 14%, 94%)',
            '200': 'hsl(30, 14%, 86%)',
            '300': 'hsl(30, 14%, 76%)',
            '400': 'hsl(30, 14%, 64%)',
            '500': 'hsl(30, 14%, 50%)',
            '600': 'hsl(30, 14%, 40%)',
            '700': 'hsl(30, 14%, 32%)',
            '800': 'hsl(30, 14%, 24%)',
            '900': 'hsl(30, 14%, 16%)',
            '950': 'hsl(30, 14%, 10%)',
            DEFAULT: '#736557'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#585048',
        'neutral-300': '#c2bbb5',
        'neutral-400': '#767676',
        'neutral-500': '#f6f6f6',
        'neutral-600': '#d9d9d9',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter',
            'sans-serif'
        ],
        body: [
            'Inter Tight',
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
                lineHeight: '22.4px',
                letterSpacing: '-0.84px'
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
                lineHeight: '23.4px',
                letterSpacing: '-1.26px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '28.6px',
                letterSpacing: '-1.82px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '44px',
                letterSpacing: '-2.8px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '100px',
                letterSpacing: '-8px'
            }
        ],
        '180': [
            '180px',
            {
                lineHeight: '144px',
                letterSpacing: '-12.6px'
            }
        ],
        '585.57': [
            '585.57px',
            {
                lineHeight: '468.456px',
                letterSpacing: '-29.2785px'
            }
        ]
    },
    spacing: {
        '15': '30px',
        '25': '50px',
        '30': '60px',
        '35': '70px',
        '50': '100px',
        '62': '124px',
        '71': '142px',
        '100': '200px',
        '109': '218px',
        '180': '360px',
        '1px': '1px',
        '5px': '5px',
        '25px': '25px',
        '35px': '35px',
        '131px': '131px'
    },
    borderRadius: {
        sm: '3px',
        md: '10px',
        lg: '15px',
        xl: '22px',
        full: '200px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px',
        lg: 'rgba(0, 0, 0, 0.25) 0px 10px 20px 0px'
    },
    screens: {
        md: '810px'
    },
    container: {
        center: true,
        padding: '50px'
    },
    maxWidth: {
        container: '1620px'
    }
},
  },
};

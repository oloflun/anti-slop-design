/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(16, 100%, 97%)',
            '100': 'hsl(16, 100%, 94%)',
            '200': 'hsl(16, 100%, 86%)',
            '300': 'hsl(16, 100%, 76%)',
            '400': 'hsl(16, 100%, 64%)',
            '500': 'hsl(16, 100%, 50%)',
            '600': 'hsl(16, 100%, 40%)',
            '700': 'hsl(16, 100%, 32%)',
            '800': 'hsl(16, 100%, 24%)',
            '900': 'hsl(16, 100%, 16%)',
            '950': 'hsl(16, 100%, 10%)',
            DEFAULT: '#ff4500'
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
            '50': 'hsl(74, 100%, 97%)',
            '100': 'hsl(74, 100%, 94%)',
            '200': 'hsl(74, 100%, 86%)',
            '300': 'hsl(74, 100%, 76%)',
            '400': 'hsl(74, 100%, 64%)',
            '500': 'hsl(74, 100%, 50%)',
            '600': 'hsl(74, 100%, 40%)',
            '700': 'hsl(74, 100%, 32%)',
            '800': 'hsl(74, 100%, 24%)',
            '900': 'hsl(74, 100%, 16%)',
            '950': 'hsl(74, 100%, 10%)',
            DEFAULT: '#d2ff37'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#0b0b0b',
        'neutral-300': '#e9e9e9',
        'neutral-400': '#767676',
        'neutral-500': '#181818',
        'neutral-600': '#222222',
        background: '#0b0b0b',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Geist',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ]
    },
    fontSize: {
        '13': [
            '13px',
            {
                lineHeight: '15.6px',
                letterSpacing: '-0.13px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18.2px',
                letterSpacing: '-0.14px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '18px',
                letterSpacing: '-0.15px'
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
                lineHeight: '14.76px',
                letterSpacing: '-0.36px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '24px',
                letterSpacing: '-0.2px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '28.6px',
                letterSpacing: '-0.26px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '35.2px',
                letterSpacing: '-0.32px'
            }
        ],
        '34': [
            '34px',
            {
                lineHeight: '30.6px',
                letterSpacing: '-2.04px'
            }
        ],
        '58': [
            '58px',
            {
                lineHeight: 'normal',
                letterSpacing: '-4.06px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: 'normal',
                letterSpacing: '-4.48px'
            }
        ],
        '78': [
            '78px',
            {
                lineHeight: 'normal',
                letterSpacing: '-5.46px'
            }
        ],
        '92': [
            '92px',
            {
                lineHeight: '75.44px',
                letterSpacing: '-4.6px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '82px',
                letterSpacing: '-4px'
            }
        ],
        '140.498': [
            '140.498px',
            {
                lineHeight: '115.208px',
                letterSpacing: '-7.02489px'
            }
        ]
    },
    spacing: {
        '15': '30px',
        '18': '36px',
        '20': '40px',
        '25': '50px',
        '30': '60px',
        '35': '70px',
        '40': '80px',
        '45': '90px',
        '50': '100px',
        '55': '110px',
        '60': '120px',
        '65': '130px',
        '1px': '1px'
    },
    borderRadius: {
        md: '10px',
        full: '100px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '810px'
    },
    transitionDuration: {
        '1': '0.001s',
        '200': '0.2s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.44, 0, 0.56, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1440px'
    }
},
  },
};

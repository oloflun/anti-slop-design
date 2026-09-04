/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(120, 100%, 97%)',
            '100': 'hsl(120, 100%, 94%)',
            '200': 'hsl(120, 100%, 86%)',
            '300': 'hsl(120, 100%, 76%)',
            '400': 'hsl(120, 100%, 64%)',
            '500': 'hsl(120, 100%, 50%)',
            '600': 'hsl(120, 100%, 40%)',
            '700': 'hsl(120, 100%, 32%)',
            '800': 'hsl(120, 100%, 24%)',
            '900': 'hsl(120, 100%, 16%)',
            '950': 'hsl(120, 100%, 10%)',
            DEFAULT: '#00a000'
        },
        secondary: {
            '50': 'hsl(13, 100%, 97%)',
            '100': 'hsl(13, 100%, 94%)',
            '200': 'hsl(13, 100%, 86%)',
            '300': 'hsl(13, 100%, 76%)',
            '400': 'hsl(13, 100%, 64%)',
            '500': 'hsl(13, 100%, 50%)',
            '600': 'hsl(13, 100%, 40%)',
            '700': 'hsl(13, 100%, 32%)',
            '800': 'hsl(13, 100%, 24%)',
            '900': 'hsl(13, 100%, 16%)',
            '950': 'hsl(13, 100%, 10%)',
            DEFAULT: '#d32c00'
        },
        accent: {
            '50': 'hsl(23, 51%, 97%)',
            '100': 'hsl(23, 51%, 94%)',
            '200': 'hsl(23, 51%, 86%)',
            '300': 'hsl(23, 51%, 76%)',
            '400': 'hsl(23, 51%, 64%)',
            '500': 'hsl(23, 51%, 50%)',
            '600': 'hsl(23, 51%, 40%)',
            '700': 'hsl(23, 51%, 32%)',
            '800': 'hsl(23, 51%, 24%)',
            '900': 'hsl(23, 51%, 16%)',
            '950': 'hsl(23, 51%, 10%)',
            DEFAULT: '#ebd2c2'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#f6f6f6',
        'neutral-300': '#242323',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter',
            'sans-serif'
        ],
        body: [
            'GTStandard-M',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: 'normal'
            }
        ],
        '11': [
            '11px',
            {
                lineHeight: '13.2px',
                letterSpacing: '0.4px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '20.4px',
                letterSpacing: '-0.8px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '19.5px',
                letterSpacing: '-0.8px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '14px',
                letterSpacing: '1px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '18px',
                letterSpacing: '-0.8px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '20px',
                letterSpacing: '-0.6px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '24px',
                letterSpacing: '-0.8px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '36px',
                letterSpacing: '-1.413px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '0px',
                letterSpacing: '-0.8px'
            }
        ],
        '44': [
            '44px',
            {
                lineHeight: '46px',
                letterSpacing: '-2px'
            }
        ],
        '55': [
            '55px',
            {
                lineHeight: '57px',
                letterSpacing: '-2.5px'
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
        '12': '24px',
        '15': '30px',
        '20': '40px',
        '22': '44px',
        '24': '48px',
        '28': '56px',
        '30': '60px',
        '35': '70px',
        '40': '80px',
        '55': '110px',
        '64': '128px',
        '128': '256px',
        '1px': '1px',
        '35px': '35px',
        '385px': '385px',
        '425px': '425px'
    },
    borderRadius: {
        full: '50px'
    },
    screens: {
        md: '750px',
        '900px': '900px',
        lg: '990px',
        '1400px': '1400px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.86, 0, 0.07, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1250px'
    }
},
  },
};

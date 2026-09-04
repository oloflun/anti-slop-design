/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(30, 12%, 97%)',
            '100': 'hsl(30, 12%, 94%)',
            '200': 'hsl(30, 12%, 86%)',
            '300': 'hsl(30, 12%, 76%)',
            '400': 'hsl(30, 12%, 64%)',
            '500': 'hsl(30, 12%, 50%)',
            '600': 'hsl(30, 12%, 40%)',
            '700': 'hsl(30, 12%, 32%)',
            '800': 'hsl(30, 12%, 24%)',
            '900': 'hsl(30, 12%, 16%)',
            '950': 'hsl(30, 12%, 10%)',
            DEFAULT: '#b8aea4'
        },
        secondary: {
            '50': 'hsl(53, 69%, 97%)',
            '100': 'hsl(53, 69%, 94%)',
            '200': 'hsl(53, 69%, 86%)',
            '300': 'hsl(53, 69%, 76%)',
            '400': 'hsl(53, 69%, 64%)',
            '500': 'hsl(53, 69%, 50%)',
            '600': 'hsl(53, 69%, 40%)',
            '700': 'hsl(53, 69%, 32%)',
            '800': 'hsl(53, 69%, 24%)',
            '900': 'hsl(53, 69%, 16%)',
            '950': 'hsl(53, 69%, 10%)',
            DEFAULT: '#fdfcf4'
        },
        accent: {
            '50': 'hsl(30, 13%, 97%)',
            '100': 'hsl(30, 13%, 94%)',
            '200': 'hsl(30, 13%, 86%)',
            '300': 'hsl(30, 13%, 76%)',
            '400': 'hsl(30, 13%, 64%)',
            '500': 'hsl(30, 13%, 50%)',
            '600': 'hsl(30, 13%, 40%)',
            '700': 'hsl(30, 13%, 32%)',
            '800': 'hsl(30, 13%, 24%)',
            '900': 'hsl(30, 13%, 16%)',
            '950': 'hsl(30, 13%, 10%)',
            DEFAULT: '#12100e'
        },
        'neutral-50': '#2d2928',
        'neutral-100': '#000000',
        'neutral-200': '#736f6a',
        'neutral-300': '#ece8e3',
        background: '#fdfcf4',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Suisse Intl',
            'sans-serif'
        ],
        body: [
            'Helvetica',
            'sans-serif'
        ],
        font2: [
            'Tobias',
            'sans-serif'
        ]
    },
    fontSize: {
        '13': [
            '13px',
            {
                lineHeight: '19.5px',
                letterSpacing: '1.56px'
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
                lineHeight: '22.5px',
                letterSpacing: '0.15px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '19': [
            '19px',
            {
                lineHeight: '22.8px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px',
                letterSpacing: '-0.2px'
            }
        ],
        '21': [
            '21px',
            {
                lineHeight: '24.15px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '60px',
                letterSpacing: '0.2px'
            }
        ],
        '46': [
            '46px',
            {
                lineHeight: '49.68px',
                letterSpacing: '-0.92px'
            }
        ],
        '76': [
            '76px',
            {
                lineHeight: '71.44px'
            }
        ],
        '82': [
            '82px',
            {
                lineHeight: '77.08px'
            }
        ],
        '15.5': [
            '15.5px',
            {
                lineHeight: '25.575px'
            }
        ],
        '14.5': [
            '14.5px',
            {
                lineHeight: '23.925px'
            }
        ],
        '13.5': [
            '13.5px',
            {
                lineHeight: '20.25px',
                letterSpacing: '0.135px'
            }
        ],
        '12.5': [
            '12.5px',
            {
                lineHeight: '17.1875px'
            }
        ]
    },
    spacing: {
        '20': '40px',
        '22': '44px',
        '24': '48px',
        '28': '56px',
        '32': '64px',
        '36': '72px',
        '40': '80px',
        '52': '104px',
        '60': '120px',
        '71': '142px',
        '75': '150px',
        '80': '160px',
        '103': '206px',
        '1px': '1px',
        '61px': '61px'
    },
    borderRadius: {
        sm: '3px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(184, 174, 164, 0.5) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px',
        xl: 'rgba(0, 0, 0, 0.25) 0px 0px 35px 0px'
    },
    screens: {
        md: '768px',
        lg: '1024px'
    },
    transitionDuration: {
        '150': '0.15s',
        '200': '0.2s',
        '280': '0.28s',
        '300': '0.3s',
        '350': '0.35s',
        '420': '0.42s',
        '450': '0.45s',
        '600': '0.6s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.65, 0, 0.35, 1)'
    },
    container: {
        center: true,
        padding: '48px'
    },
    maxWidth: {
        container: '1440px'
    }
},
  },
};

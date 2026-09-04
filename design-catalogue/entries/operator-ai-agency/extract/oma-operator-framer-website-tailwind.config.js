/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
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
        secondary: {
            '50': 'hsl(155, 89%, 97%)',
            '100': 'hsl(155, 89%, 94%)',
            '200': 'hsl(155, 89%, 86%)',
            '300': 'hsl(155, 89%, 76%)',
            '400': 'hsl(155, 89%, 64%)',
            '500': 'hsl(155, 89%, 50%)',
            '600': 'hsl(155, 89%, 40%)',
            '700': 'hsl(155, 89%, 32%)',
            '800': 'hsl(155, 89%, 24%)',
            '900': 'hsl(155, 89%, 16%)',
            '950': 'hsl(155, 89%, 10%)',
            DEFAULT: '#0eea8e'
        },
        'neutral-50': '#000000',
        'neutral-100': '#74797d',
        'neutral-200': '#fafafa',
        'neutral-300': '#d4d6d8',
        'neutral-400': '#f4f5f5',
        'neutral-500': '#08090a',
        'neutral-600': '#a1a5aa',
        'neutral-700': '#181a1b',
        'neutral-800': '#e4e6e7',
        'neutral-900': '#52575b',
        background: '#08090a',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Uncut Sans Medium',
            'sans-serif'
        ],
        body: [
            'Inter',
            'sans-serif'
        ]
    },
    fontSize: {
        '11': [
            '11px',
            {
                lineHeight: '11px',
                letterSpacing: '0.11px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: 'normal'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '18.85px',
                letterSpacing: '-0.195px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '16.8px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '21px',
                letterSpacing: '-0.3px'
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
                lineHeight: '24.3px',
                letterSpacing: '-0.54px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px',
                letterSpacing: '-0.4px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '28.6px',
                letterSpacing: '-0.66px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '32.5px',
                letterSpacing: '-0.91px'
            }
        ],
        '31': [
            '31px',
            {
                lineHeight: '35.65px',
                letterSpacing: '-1.24px'
            }
        ],
        '37': [
            '37px',
            {
                lineHeight: '40.7px',
                letterSpacing: '-1.665px'
            }
        ],
        '45': [
            '45px',
            {
                lineHeight: '47.25px',
                letterSpacing: '-2.25px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '64px',
                letterSpacing: '-3.84px'
            }
        ]
    },
    spacing: {
        '8': '32px',
        '12': '48px',
        '20': '80px',
        '30': '120px',
        '1px': '1px',
        '61px': '61px',
        '99px': '99px'
    },
    borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '11px',
        full: '100px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(46, 255, 157, 0.3) 0px 0px 3px 0px, rgba(255, 255, 255, 0.2) 0px 2px 7px 0px',
        md: 'rgba(0, 0, 0, 0.1) 0px 4px 10px 0px',
        xl: 'rgba(0, 0, 0, 0.37) -62px 16px 141px 0px, rgba(0, 0, 0, 0.32) -247px 64px 250px 0px, rgba(0, 0, 0, 0.19) -557px 145px 250px 0px, rgba(0, 0, 0, 0.06) -990px 257px 250px 0px, rgba(0, 0, 0, 0.01) -1546px 402px 250px 0px'
    },
    screens: {
        md: '810px'
    },
    transitionDuration: {
        '1': '0.001s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1400px'
    }
},
  },
};

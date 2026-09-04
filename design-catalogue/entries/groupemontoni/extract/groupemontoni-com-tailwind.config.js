/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(161, 100%, 97%)',
            '100': 'hsl(161, 100%, 94%)',
            '200': 'hsl(161, 100%, 86%)',
            '300': 'hsl(161, 100%, 76%)',
            '400': 'hsl(161, 100%, 64%)',
            '500': 'hsl(161, 100%, 50%)',
            '600': 'hsl(161, 100%, 40%)',
            '700': 'hsl(161, 100%, 32%)',
            '800': 'hsl(161, 100%, 24%)',
            '900': 'hsl(161, 100%, 16%)',
            '950': 'hsl(161, 100%, 10%)',
            DEFAULT: '#008057'
        },
        secondary: {
            '50': 'hsl(195, 63%, 97%)',
            '100': 'hsl(195, 63%, 94%)',
            '200': 'hsl(195, 63%, 86%)',
            '300': 'hsl(195, 63%, 76%)',
            '400': 'hsl(195, 63%, 64%)',
            '500': 'hsl(195, 63%, 50%)',
            '600': 'hsl(195, 63%, 40%)',
            '700': 'hsl(195, 63%, 32%)',
            '800': 'hsl(195, 63%, 24%)',
            '900': 'hsl(195, 63%, 16%)',
            '950': 'hsl(195, 63%, 10%)',
            DEFAULT: '#123f4e'
        },
        accent: {
            '50': 'hsl(38, 36%, 97%)',
            '100': 'hsl(38, 36%, 94%)',
            '200': 'hsl(38, 36%, 86%)',
            '300': 'hsl(38, 36%, 76%)',
            '400': 'hsl(38, 36%, 64%)',
            '500': 'hsl(38, 36%, 50%)',
            '600': 'hsl(38, 36%, 40%)',
            '700': 'hsl(38, 36%, 32%)',
            '800': 'hsl(38, 36%, 24%)',
            '900': 'hsl(38, 36%, 16%)',
            '950': 'hsl(38, 36%, 10%)',
            DEFAULT: '#b99c6a'
        },
        'neutral-50': '#000000',
        'neutral-100': '#0d0d0d',
        'neutral-200': '#ffffff',
        'neutral-300': '#81907a',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'studiopro',
            'sans-serif'
        ],
        heading: [
            'fkroman',
            'sans-serif'
        ]
    },
    fontSize: {
        '8': [
            '8px',
            {
                lineHeight: '12px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px',
                letterSpacing: '-0.32px'
            }
        ],
        '57.6': [
            '57.6px',
            {
                lineHeight: '63.36px',
                letterSpacing: '-1.152px'
            }
        ],
        '25.6': [
            '25.6px',
            {
                lineHeight: '28.16px',
                letterSpacing: '-0.512px'
            }
        ],
        '20.8': [
            '20.8px',
            {
                lineHeight: '22.88px',
                letterSpacing: '-0.416px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '28.8px',
                letterSpacing: '-0.256px'
            }
        ],
        '12.8': [
            '12.8px',
            {
                lineHeight: '12.8px'
            }
        ],
        '11.2': [
            '11.2px',
            {
                lineHeight: '11.2px'
            }
        ],
        '9.6': [
            '9.6px',
            {
                lineHeight: '9.6px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '13': '26px',
        '16': '32px',
        '19': '38px',
        '40': '80px',
        '51': '102px',
        '64': '128px',
        '19px': '19px',
        '61px': '61px'
    },
    borderRadius: {
        md: '6px',
        full: '9999px'
    },
    screens: {
        xs: '360px',
        sm: '620px',
        md: '800px',
        '890px': '890px',
        '1120px': '1120px',
        '1360px': '1360px',
        '2xl': '1600px',
        '1920px': '1920px',
        '2048px': '2048px',
        '3840px': '3840px'
    },
    transitionDuration: {
        '0': '0s',
        '150': '0.15s',
        '500': '0.5s',
        '700': '0.7s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.19, 1, 0.22, 1)',
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

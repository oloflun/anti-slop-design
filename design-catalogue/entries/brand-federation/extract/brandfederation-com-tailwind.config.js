/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(21, 91%, 97%)',
            '100': 'hsl(21, 91%, 94%)',
            '200': 'hsl(21, 91%, 86%)',
            '300': 'hsl(21, 91%, 76%)',
            '400': 'hsl(21, 91%, 64%)',
            '500': 'hsl(21, 91%, 50%)',
            '600': 'hsl(21, 91%, 40%)',
            '700': 'hsl(21, 91%, 32%)',
            '800': 'hsl(21, 91%, 24%)',
            '900': 'hsl(21, 91%, 16%)',
            '950': 'hsl(21, 91%, 10%)',
            DEFAULT: '#f56b20'
        },
        secondary: {
            '50': 'hsl(211, 55%, 97%)',
            '100': 'hsl(211, 55%, 94%)',
            '200': 'hsl(211, 55%, 86%)',
            '300': 'hsl(211, 55%, 76%)',
            '400': 'hsl(211, 55%, 64%)',
            '500': 'hsl(211, 55%, 50%)',
            '600': 'hsl(211, 55%, 40%)',
            '700': 'hsl(211, 55%, 32%)',
            '800': 'hsl(211, 55%, 24%)',
            '900': 'hsl(211, 55%, 16%)',
            '950': 'hsl(211, 55%, 10%)',
            DEFAULT: '#12273e'
        },
        accent: {
            '50': 'hsl(212, 87%, 97%)',
            '100': 'hsl(212, 87%, 94%)',
            '200': 'hsl(212, 87%, 86%)',
            '300': 'hsl(212, 87%, 76%)',
            '400': 'hsl(212, 87%, 64%)',
            '500': 'hsl(212, 87%, 50%)',
            '600': 'hsl(212, 87%, 40%)',
            '700': 'hsl(212, 87%, 32%)',
            '800': 'hsl(212, 87%, 24%)',
            '900': 'hsl(212, 87%, 16%)',
            '950': 'hsl(212, 87%, 10%)',
            DEFAULT: '#083a74'
        },
        'neutral-50': '#333333',
        'neutral-100': '#ffffff',
        'neutral-200': '#000000',
        'neutral-300': '#edecee',
        'neutral-400': '#222222',
        'neutral-500': '#a397af',
        'neutral-600': '#717d8b',
        'neutral-700': '#dddddd',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'webflow-icons',
            'sans-serif'
        ],
        font2: [
            'Manrope',
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
        '67.0476': [
            '67.0476px',
            {
                lineHeight: '80.4571px'
            }
        ],
        '36.5714': [
            '36.5714px',
            {
                lineHeight: '43.8857px'
            }
        ],
        '30.4762': [
            '30.4762px',
            {
                lineHeight: '39.619px'
            }
        ],
        '24.381': [
            '24.381px',
            {
                lineHeight: '34.1333px'
            }
        ],
        '21.3333': [
            '21.3333px',
            {
                lineHeight: '27.7333px'
            }
        ],
        '15.4286': [
            '15.4286px',
            {
                lineHeight: '19.2857px',
                letterSpacing: '-0.26px'
            }
        ],
        '13.7143': [
            '13.7143px',
            {
                lineHeight: '17.1429px',
                letterSpacing: '-0.26px'
            }
        ],
        '12.1905': [
            '12.1905px',
            {
                lineHeight: '20px'
            }
        ],
        '9.14286': [
            '9.14286px',
            {
                lineHeight: '20px',
                letterSpacing: '0.8px'
            }
        ],
        '8.22857': [
            '8.22857px',
            {
                lineHeight: '20px',
                letterSpacing: '0.8px'
            }
        ]
    },
    spacing: {
        '0': '1px',
        '1': '6px',
        '2': '24px',
        '3': '37px',
        '4': '48px',
        '5': '53px',
        '6': '61px',
        '7': '69px',
        '8': '79px',
        '9': '85px',
        '10': '98px',
        '11': '104px',
        '12': '107px',
        '13': '128px',
        '14': '158px',
        '15': '192px',
        '16': '195px',
        '17': '256px'
    },
    borderRadius: {
        lg: '12px',
        xl: '20px',
        full: '2000px'
    },
    screens: {
        md: '768px',
        '1680px': '1680px'
    },
    transitionDuration: {
        '200': '0.2s',
        '325': '0.325s',
        '350': '0.35s'
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

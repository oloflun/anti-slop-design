/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(38, 26%, 97%)',
            '100': 'hsl(38, 26%, 94%)',
            '200': 'hsl(38, 26%, 86%)',
            '300': 'hsl(38, 26%, 76%)',
            '400': 'hsl(38, 26%, 64%)',
            '500': 'hsl(38, 26%, 50%)',
            '600': 'hsl(38, 26%, 40%)',
            '700': 'hsl(38, 26%, 32%)',
            '800': 'hsl(38, 26%, 24%)',
            '900': 'hsl(38, 26%, 16%)',
            '950': 'hsl(38, 26%, 10%)',
            DEFAULT: '#dfd7c9'
        },
        secondary: {
            '50': 'hsl(137, 37%, 97%)',
            '100': 'hsl(137, 37%, 94%)',
            '200': 'hsl(137, 37%, 86%)',
            '300': 'hsl(137, 37%, 76%)',
            '400': 'hsl(137, 37%, 64%)',
            '500': 'hsl(137, 37%, 50%)',
            '600': 'hsl(137, 37%, 40%)',
            '700': 'hsl(137, 37%, 32%)',
            '800': 'hsl(137, 37%, 24%)',
            '900': 'hsl(137, 37%, 16%)',
            '950': 'hsl(137, 37%, 10%)',
            DEFAULT: '#20462b'
        },
        accent: {
            '50': 'hsl(136, 37%, 97%)',
            '100': 'hsl(136, 37%, 94%)',
            '200': 'hsl(136, 37%, 86%)',
            '300': 'hsl(136, 37%, 76%)',
            '400': 'hsl(136, 37%, 64%)',
            '500': 'hsl(136, 37%, 50%)',
            '600': 'hsl(136, 37%, 40%)',
            '700': 'hsl(136, 37%, 32%)',
            '800': 'hsl(136, 37%, 24%)',
            '900': 'hsl(136, 37%, 16%)',
            '950': 'hsl(136, 37%, 10%)',
            DEFAULT: '#1a3822'
        },
        'neutral-50': '#303030',
        'neutral-100': '#000000',
        background: '#dfd7c9',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Aime',
            'sans-serif'
        ],
        body: [
            'NM',
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
        '32': [
            '32px',
            {
                lineHeight: '38.4px',
                letterSpacing: '-0.96px'
            }
        ],
        '75.52': [
            '75.52px',
            {
                lineHeight: '64.192px',
                letterSpacing: '-3.776px'
            }
        ],
        '74.24': [
            '74.24px',
            {
                lineHeight: '63.104px',
                letterSpacing: '-3.712px'
            }
        ],
        '61.44': [
            '61.44px',
            {
                lineHeight: '55.296px',
                letterSpacing: '-2.4576px'
            }
        ],
        '58.88': [
            '58.88px',
            {
                lineHeight: '52.992px',
                letterSpacing: '-2.3552px'
            }
        ],
        '51.2': [
            '51.2px',
            {
                lineHeight: '46.08px',
                letterSpacing: '-2.048px'
            }
        ],
        '40.96': [
            '40.96px',
            {
                lineHeight: '36.864px',
                letterSpacing: '-1.2288px'
            }
        ],
        '40.32': [
            '40.32px',
            {
                lineHeight: '36.288px',
                letterSpacing: '-1.2096px'
            }
        ],
        '39.68': [
            '39.68px',
            {
                lineHeight: '35.712px',
                letterSpacing: '-1.5872px'
            }
        ],
        '35.84': [
            '35.84px',
            {
                lineHeight: '35.84px',
                letterSpacing: '-1.4336px'
            }
        ],
        '26.88': [
            '26.88px',
            {
                lineHeight: '28.224px',
                letterSpacing: '-0.512px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '20.16px',
                letterSpacing: '-0.384px'
            }
        ],
        '16.64': [
            '16.64px',
            {
                lineHeight: '17.472px'
            }
        ],
        '12.8': [
            '12.8px',
            {
                lineHeight: '13.44px',
                letterSpacing: '-0.512px'
            }
        ]
    },
    spacing: {
        '12': '24px',
        '21': '42px',
        '25': '50px',
        '43': '86px',
        '60': '120px',
        '76': '152px',
        '91': '182px',
        '96': '192px',
        '127': '254px',
        '140': '280px',
        '160': '320px',
        '192': '384px',
        '1px': '1px',
        '73px': '73px',
        '77px': '77px',
        '141px': '141px',
        '217px': '217px',
        '313px': '313px',
        '379px': '379px'
    },
    borderRadius: {
        xs: '2px',
        full: '100px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '400': '0.4s',
        '450': '0.45s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1280px'
    }
},
  },
};

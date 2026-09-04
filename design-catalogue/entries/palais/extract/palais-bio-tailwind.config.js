/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(221, 59%, 97%)',
            '100': 'hsl(221, 59%, 94%)',
            '200': 'hsl(221, 59%, 86%)',
            '300': 'hsl(221, 59%, 76%)',
            '400': 'hsl(221, 59%, 64%)',
            '500': 'hsl(221, 59%, 50%)',
            '600': 'hsl(221, 59%, 40%)',
            '700': 'hsl(221, 59%, 32%)',
            '800': 'hsl(221, 59%, 24%)',
            '900': 'hsl(221, 59%, 16%)',
            '950': 'hsl(221, 59%, 10%)',
            DEFAULT: '#234386'
        },
        secondary: {
            '50': 'hsl(92, 60%, 97%)',
            '100': 'hsl(92, 60%, 94%)',
            '200': 'hsl(92, 60%, 86%)',
            '300': 'hsl(92, 60%, 76%)',
            '400': 'hsl(92, 60%, 64%)',
            '500': 'hsl(92, 60%, 50%)',
            '600': 'hsl(92, 60%, 40%)',
            '700': 'hsl(92, 60%, 32%)',
            '800': 'hsl(92, 60%, 24%)',
            '900': 'hsl(92, 60%, 16%)',
            '950': 'hsl(92, 60%, 10%)',
            DEFAULT: '#61a229'
        },
        accent: {
            '50': 'hsl(202, 100%, 97%)',
            '100': 'hsl(202, 100%, 94%)',
            '200': 'hsl(202, 100%, 86%)',
            '300': 'hsl(202, 100%, 76%)',
            '400': 'hsl(202, 100%, 64%)',
            '500': 'hsl(202, 100%, 50%)',
            '600': 'hsl(202, 100%, 40%)',
            '700': 'hsl(202, 100%, 32%)',
            '800': 'hsl(202, 100%, 24%)',
            '900': 'hsl(202, 100%, 16%)',
            '950': 'hsl(202, 100%, 10%)',
            DEFAULT: '#00578a'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#212529',
        'neutral-300': '#333333',
        'neutral-400': '#f3f5f7',
        'neutral-500': '#3a4856',
        'neutral-600': '#e3e1e8',
        'neutral-700': '#898989',
        'neutral-800': '#111111',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Times New Roman',
            'sans-serif'
        ],
        body: [
            'ITC Avant Garde Std Bk',
            'sans-serif'
        ],
        font2: [
            'Sonder Sans Black Rough',
            'sans-serif'
        ],
        font4: [
            'Delivery Note DEMO',
            'sans-serif'
        ],
        font5: [
            'hwt-artz',
            'sans-serif'
        ],
        font8: [
            'Sandman_Fill',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: 'normal',
                letterSpacing: '2px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '24px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '17': [
            '17px',
            {
                lineHeight: '17px',
                letterSpacing: '1px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: 'normal',
                letterSpacing: '2px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '32px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '32px',
                letterSpacing: '1.6px'
            }
        ],
        '33': [
            '33px',
            {
                lineHeight: '39px'
            }
        ],
        '46': [
            '46px',
            {
                lineHeight: '40px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '40px'
            }
        ],
        '50': [
            '50px',
            {
                lineHeight: '44px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '56px'
            }
        ],
        '73': [
            '73px',
            {
                lineHeight: '54px'
            }
        ],
        '14.6667': [
            '14.6667px',
            {
                lineHeight: '18px'
            }
        ],
        '14.4': [
            '14.4px',
            {
                lineHeight: '24px',
                letterSpacing: '2px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '15': '30px',
        '24': '48px',
        '32': '64px',
        '35': '70px',
        '40': '80px',
        '45': '90px',
        '50': '100px',
        '52': '104px',
        '55': '110px',
        '60': '120px',
        '64': '128px',
        '72': '144px',
        '75': '150px',
        '80': '160px',
        '88': '176px',
        '90': '180px',
        '100': '200px',
        '120': '240px',
        '220': '440px',
        '37px': '37px',
        '211px': '211px'
    },
    borderRadius: {
        xs: '2px',
        sm: '5px',
        md: '8px',
        lg: '16px',
        full: '50px'
    },
    boxShadow: {
        sm: 'rgb(22, 22, 22) 2px 2px 5px 2px',
        md: 'rgba(172, 171, 171, 0.3) 0px -1px 10px 0px',
        xl: 'rgba(0, 0, 0, 0.16) -14px 10px 49px 0px'
    },
    screens: {
        xs: '380px',
        '393px': '393px',
        '400px': '400px',
        sm: '646px',
        '562px': '562px',
        md: '783px',
        '847px': '847px',
        '868px': '868px',
        lg: '1080px',
        xl: '1341px',
        '2xl': '1600px',
        '1684px': '1684px',
        '1700px': '1700px',
        '1708px': '1708px',
        '1750px': '1750px',
        '1800px': '1800px',
        '1875px': '1875px',
        '1880px': '1880px',
        '1900px': '1900px',
        '2000px': '2000px'
    },
    transitionDuration: {
        '0': '0s',
        '150': '0.15s',
        '200': '0.2s',
        '300': '0.3s',
        '350': '0.35s',
        '400': '0.4s',
        '500': '0.5s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.3, 0.95, 0.33, 0.98)',
        linear: 'linear'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '447px'
    }
},
  },
};

/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#e5e7eb',
        'neutral-100': '#222222',
        'neutral-200': '#000000',
        'neutral-300': '#343434',
        'neutral-400': '#aaaaaa',
        'neutral-500': '#dbdbdb',
        'neutral-600': '#cccccc',
        background: '#343434',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'TT Hoves Pro Trial',
            'sans-serif'
        ],
        body: [
            'NeueMontreal',
            'sans-serif'
        ]
    },
    fontSize: {
        '6': [
            '6px',
            {
                lineHeight: '9px',
                letterSpacing: '1.32px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '24px',
                letterSpacing: '5.28px'
            }
        ],
        '21.3334': [
            '21.3334px',
            {
                lineHeight: '32.0001px'
            }
        ],
        '17.7778': [
            '17.7778px',
            {
                lineHeight: '26.6667px',
                letterSpacing: '1.77778px'
            }
        ],
        '14.2222': [
            '14.2222px',
            {
                lineHeight: '21.3333px'
            }
        ],
        '12.4444': [
            '12.4444px',
            {
                lineHeight: '18.6666px'
            }
        ],
        '9.77779': [
            '9.77779px',
            {
                lineHeight: '14.6667px'
            }
        ],
        '8.88889': [
            '8.88889px',
            {
                lineHeight: '13.3333px',
                letterSpacing: '1.95556px'
            }
        ],
        '8.88883': [
            '8.88883px',
            {
                lineHeight: '8.88883px',
                letterSpacing: '1.95554px'
            }
        ],
        '7.11117': [
            '7.11117px',
            {
                lineHeight: '10.6668px',
                letterSpacing: '1.56446px'
            }
        ]
    },
    spacing: {
        '2': '4px',
        '25': '50px',
        '57': '114px',
        '62': '124px',
        '68': '136px',
        '80': '160px',
        '191': '382px',
        '43px': '43px',
        '57px': '57px',
        '71px': '71px',
        '89px': '89px'
    },
    screens: {
        sm: '640px',
        lg: '1024px',
        '1200px': '1200px',
        '2400px': '2400px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s',
        '800': '0.8s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        default: 'ease',
        linear: 'linear',
        custom: 'cubic-bezier(0.645, 0.045, 0.355, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '2400px'
    }
},
  },
};

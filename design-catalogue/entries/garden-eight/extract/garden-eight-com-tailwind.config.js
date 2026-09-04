/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#dbd6d0',
        'neutral-100': '#1e1f1f',
        background: '#1e1f1f',
        foreground: '#dbd6d0'
    },
    fontFamily: {
        sans: [
            'lausanne',
            'sans-serif'
        ],
        body: [
            'gunsan',
            'sans-serif'
        ]
    },
    fontSize: {
        '0': [
            '0px',
            {
                lineHeight: '0px'
            }
        ],
        '191.104': [
            '191.104px',
            {
                lineHeight: '271.368px'
            }
        ],
        '14.85': [
            '14.85px',
            {
                lineHeight: '21.087px'
            }
        ],
        '13.05': [
            '13.05px',
            {
                lineHeight: '18.531px'
            }
        ],
        '11.7': [
            '11.7px',
            {
                lineHeight: '18.72px'
            }
        ]
    },
    spacing: {
        '20': '40px',
        '23': '46px',
        '38': '76px',
        '70': '140px',
        '80': '160px',
        '124': '248px',
        '1px': '1px',
        '23px': '23px',
        '53px': '53px',
        '185px': '185px'
    },
    borderRadius: {
        full: '1280px'
    },
    boxShadow: {
        sm: 'rgb(30, 31, 31) 0px 2px 2px 0px inset, rgb(219, 214, 208) 0px 3px 2px 0px inset, rgb(219, 214, 208) 0px 3px 3px 0px inset'
    },
    screens: {
        xs: '321px',
        '1680px': '1680px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '0': '0s',
        '50': '0.05s',
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '600': '0.6s',
        '700': '0.7s',
        '1400': '1.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.32, 0.94, 0.6, 1)'
    }
},
  },
};

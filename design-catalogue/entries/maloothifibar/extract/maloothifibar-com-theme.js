// React Theme — extracted from https://www.maloothifibar.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '14': string;
    '49': string;
    '22.75': string;
    '17.5': string;
    '15.75': string;
    '12.25': string;
    '10.5': string;
 *   };
 *   space: {
    '1': string;
    '28': string;
    '35': string;
    '70': string;
    '88': string;
    '105': string;
    '112': string;
    '119': string;
    '140': string;
    '154': string;
    '168': string;
    '175': string;
    '191': string;
    '201': string;
    '236': string;
    '252': string;
 *   };
 *   radii: {

 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#191313",
    "background": "#a8a99e",
    "foreground": "#000000",
    "neutral50": "#efeeec",
    "neutral100": "#a8a99e",
    "neutral200": "#000000"
  },
  "fonts": {
    "body": "'Inter Tight', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "49": "49px",
    "22.75": "22.75px",
    "17.5": "17.5px",
    "15.75": "15.75px",
    "12.25": "12.25px",
    "10.5": "10.5px"
  },
  "space": {
    "1": "1px",
    "28": "28px",
    "35": "35px",
    "70": "70px",
    "88": "88px",
    "105": "105px",
    "112": "112px",
    "119": "119px",
    "140": "140px",
    "154": "154px",
    "168": "168px",
    "175": "175px",
    "191": "191px",
    "201": "201px",
    "236": "236px",
    "252": "252px"
  },
  "radii": {},
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#191313",
      "light": "hsl(0, 14%, 24%)",
      "dark": "hsl(0, 14%, 10%)"
    },
    "background": {
      "default": "#a8a99e",
      "paper": "#191313"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#191313"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "49px",
      "fontWeight": "300",
      "lineHeight": "49px"
    },
    "h3": {
      "fontSize": "22.75px",
      "fontWeight": "700",
      "lineHeight": "22.75px"
    },
    "body1": {
      "fontSize": "17.5px",
      "fontWeight": "700",
      "lineHeight": "17.5px"
    },
    "body2": {
      "fontSize": "12.25px",
      "fontWeight": "300",
      "lineHeight": "14.7px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;

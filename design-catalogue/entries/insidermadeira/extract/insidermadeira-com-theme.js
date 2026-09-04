// React Theme — extracted from https://www.insidermadeira.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '10': string;
    '14': string;
    '16': string;
    '21': string;
    '24': string;
    '36': string;
    '63.3333': string;
    '23.4667': string;
    '12.8': string;
    '10.6667': string;
    '9.33333': string;
    '6.66667': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '27': string;
    '30': string;
    '40': string;
    '53': string;
    '60': string;
    '67': string;
    '80': string;
    '85': string;
    '93': string;
    '100': string;
    '103': string;
    '149': string;
    '297': string;
    '333': string;
 *   };
 *   radii: {
    sm: string;
    xl: string;
    full: string;
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
    "primary": "#ffdede",
    "secondary": "#f1ede5",
    "background": "#f9f9f9",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#201f1d",
    "neutral200": "#ffffff",
    "neutral300": "#c6c3bb",
    "neutral400": "#333333",
    "neutral500": "#dddddd",
    "neutral600": "#b8b8b8",
    "neutral700": "#6a6a6a",
    "neutral800": "#cccccc"
  },
  "fonts": {
    "body": "'GT Super Display', sans-serif"
  },
  "fontSizes": {
    "10": "10px",
    "14": "14px",
    "16": "16px",
    "21": "21px",
    "24": "24px",
    "36": "36px",
    "63.3333": "63.3333px",
    "23.4667": "23.4667px",
    "12.8": "12.8px",
    "10.6667": "10.6667px",
    "9.33333": "9.33333px",
    "6.66667": "6.66667px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "27": "27px",
    "30": "30px",
    "40": "40px",
    "53": "53px",
    "60": "60px",
    "67": "67px",
    "80": "80px",
    "85": "85px",
    "93": "93px",
    "100": "100px",
    "103": "103px",
    "149": "149px",
    "297": "297px",
    "333": "333px"
  },
  "radii": {
    "sm": "3px",
    "xl": "20px",
    "full": "15984px"
  },
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
      "main": "#ffdede",
      "light": "hsl(0, 100%, 95%)",
      "dark": "hsl(0, 100%, 79%)"
    },
    "secondary": {
      "main": "#f1ede5",
      "light": "hsl(40, 30%, 95%)",
      "dark": "hsl(40, 30%, 77%)"
    },
    "background": {
      "default": "#f9f9f9",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#201f1d"
    }
  },
  "typography": {
    "fontFamily": "'PP Mori', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "300",
      "lineHeight": "36px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "31.2px"
    },
    "h3": {
      "fontSize": "21px",
      "fontWeight": "400",
      "lineHeight": "27.3px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "normal"
    }
  },
  "shape": {
    "borderRadius": 3
  },
  "shadows": []
};

export default theme;

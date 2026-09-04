// React Theme — extracted from https://notreal.tv/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '15': string;
    '18': string;
    '20': string;
    '22': string;
    '25': string;
    '28': string;
    '32': string;
    '38': string;
    '25.5': string;
    '23.94': string;
    '18.5395': string;
    '18.176': string;
 *   };
 *   space: {
    '1': string;
    '30': string;
    '40': string;
    '63': string;
    '80': string;
    '100': string;
    '110': string;
    '150': string;
    '300': string;
    '400': string;
    '410': string;
 *   };
 *   radii: {
    xs: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
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
    "background": "#f2f2f2",
    "foreground": "#292a2c",
    "neutral50": "#292a2c",
    "neutral100": "#000000",
    "neutral200": "#ffffff",
    "neutral300": "#999999",
    "neutral400": "#f2f2f2",
    "neutral500": "#cccccc"
  },
  "fonts": {
    "body": "'Arial', sans-serif"
  },
  "fontSizes": {
    "15": "15px",
    "18": "18px",
    "20": "20px",
    "22": "22px",
    "25": "25px",
    "28": "28px",
    "32": "32px",
    "38": "38px",
    "25.5": "25.5px",
    "23.94": "23.94px",
    "18.5395": "18.5395px",
    "18.176": "18.176px"
  },
  "space": {
    "1": "1px",
    "30": "30px",
    "40": "40px",
    "63": "63px",
    "80": "80px",
    "100": "100px",
    "110": "110px",
    "150": "150px",
    "300": "300px",
    "400": "400px",
    "410": "410px"
  },
  "radii": {
    "xs": "2px",
    "full": "50px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0.25) 0px 1.99998px 5.00004px 0px"
  },
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
    "background": {
      "default": "#f2f2f2",
      "paper": "#f2f2f2"
    },
    "text": {
      "primary": "#292a2c",
      "secondary": "#000000"
    }
  },
  "typography": {
    "fontFamily": "'Open Sans', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "32px"
    },
    "h2": {
      "fontSize": "25px",
      "fontWeight": "400",
      "lineHeight": "25px"
    },
    "h3": {
      "fontSize": "23.94px",
      "fontWeight": "400",
      "lineHeight": "35.91px"
    }
  },
  "shape": {
    "borderRadius": 2
  },
  "shadows": [
    "rgba(0, 0, 0, 0.25) 0px 1.99998px 5.00004px 0px"
  ]
};

export default theme;

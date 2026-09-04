// React Theme — extracted from https://www.nglm.com
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
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '28': string;
    '56': string;
    '80': string;
    '140.8': string;
    '102.4': string;
    '83.2': string;
 *   };
 *   space: {
    '2': string;
    '64': string;
    '80': string;
    '104': string;
    '176': string;
    '344': string;
 *   };
 *   radii: {
    xs: string;
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
    "background": "#fcfcfc",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#51585c",
    "neutral200": "#fcfcfc",
    "neutral300": "#c0c3c3",
    "neutral400": "#707575",
    "neutral500": "#131516"
  },
  "fonts": {
    "body": "'GD Trio Display', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "28": "28px",
    "56": "56px",
    "80": "80px",
    "140.8": "140.8px",
    "102.4": "102.4px",
    "83.2": "83.2px"
  },
  "space": {
    "2": "2px",
    "64": "64px",
    "80": "80px",
    "104": "104px",
    "176": "176px",
    "344": "344px"
  },
  "radii": {
    "xs": "2px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0.2) 0px 0px 4px 0px"
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
      "default": "#fcfcfc",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#fcfcfc"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "56px",
      "fontWeight": "400",
      "lineHeight": "53.76px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "400",
      "lineHeight": "30.8px"
    }
  },
  "shape": {
    "borderRadius": 2
  },
  "shadows": [
    "rgb(252, 252, 252) 0px 0px 0px 1px inset",
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.2) 0px 0px 4px 0px"
  ]
};

export default theme;

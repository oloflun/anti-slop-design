// React Theme — extracted from https://www.withshepherd.com/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
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
    '16': string;
    '24': string;
    '45': string;
    '85': string;
    '100': string;
    '23.8': string;
    '18.4': string;
    '15.5': string;
 *   };
 *   space: {
    '2': string;
    '40': string;
    '53': string;
    '58': string;
    '69': string;
    '79': string;
    '84': string;
    '92': string;
    '115': string;
    '126': string;
    '208': string;
    '409': string;
 *   };
 *   radii: {
    md: string;
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
    "primary": "#fdc331",
    "secondary": "#d6c5b5",
    "accent": "#fa9742",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#e7e7e7"
  },
  "fonts": {
    "body": "'Gt Planar Trial', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "24": "24px",
    "45": "45px",
    "85": "85px",
    "100": "100px",
    "23.8": "23.8px",
    "18.4": "18.4px",
    "15.5": "15.5px"
  },
  "space": {
    "2": "2px",
    "40": "40px",
    "53": "53px",
    "58": "58px",
    "69": "69px",
    "79": "79px",
    "84": "84px",
    "92": "92px",
    "115": "115px",
    "126": "126px",
    "208": "208px",
    "409": "409px"
  },
  "radii": {
    "md": "8px"
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
      "main": "#fdc331",
      "light": "hsl(43, 98%, 74%)",
      "dark": "hsl(43, 98%, 44%)"
    },
    "secondary": {
      "main": "#d6c5b5",
      "light": "hsl(29, 29%, 92%)",
      "dark": "hsl(29, 29%, 62%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#fdc331"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "45px",
      "fontWeight": "500",
      "lineHeight": "45px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "26.4px"
    },
    "h3": {
      "fontSize": "23.8px",
      "fontWeight": "400",
      "lineHeight": "26.18px"
    },
    "body1": {
      "fontSize": "18.4px",
      "fontWeight": "400",
      "lineHeight": "20.24px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": []
};

export default theme;

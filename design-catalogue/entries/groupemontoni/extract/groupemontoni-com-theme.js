// React Theme — extracted from https://groupemontoni.com
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
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '8': string;
    '16': string;
    '57.6': string;
    '25.6': string;
    '20.8': string;
    '19.2': string;
    '12.8': string;
    '11.2': string;
    '9.6': string;
 *   };
 *   space: {
    '2': string;
    '19': string;
    '26': string;
    '32': string;
    '38': string;
    '61': string;
    '80': string;
    '102': string;
    '128': string;
 *   };
 *   radii: {
    md: string;
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
    "primary": "#008057",
    "secondary": "#123f4e",
    "accent": "#b99c6a",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#0d0d0d",
    "neutral200": "#ffffff",
    "neutral300": "#81907a"
  },
  "fonts": {
    "body": "'fkroman', sans-serif"
  },
  "fontSizes": {
    "8": "8px",
    "16": "16px",
    "57.6": "57.6px",
    "25.6": "25.6px",
    "20.8": "20.8px",
    "19.2": "19.2px",
    "12.8": "12.8px",
    "11.2": "11.2px",
    "9.6": "9.6px"
  },
  "space": {
    "2": "2px",
    "19": "19px",
    "26": "26px",
    "32": "32px",
    "38": "38px",
    "61": "61px",
    "80": "80px",
    "102": "102px",
    "128": "128px"
  },
  "radii": {
    "md": "6px",
    "full": "9999px"
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
      "main": "#008057",
      "light": "hsl(161, 100%, 40%)",
      "dark": "hsl(161, 100%, 10%)"
    },
    "secondary": {
      "main": "#123f4e",
      "light": "hsl(195, 63%, 34%)",
      "dark": "hsl(195, 63%, 10%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#0d0d0d"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0d0d0d"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "57.6px",
      "fontWeight": "500",
      "lineHeight": "63.36px"
    },
    "h2": {
      "fontSize": "25.6px",
      "fontWeight": "500",
      "lineHeight": "28.16px"
    },
    "h3": {
      "fontSize": "20.8px",
      "fontWeight": "500",
      "lineHeight": "22.88px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "500",
      "lineHeight": "24px"
    },
    "body2": {
      "fontSize": "12.8px",
      "fontWeight": "400",
      "lineHeight": "12.8px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": []
};

export default theme;

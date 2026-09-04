// React Theme — extracted from https://deonlibra.com
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
    '15': string;
    '16': string;
    '18': string;
    '22': string;
    '28': string;
    '32': string;
    '40': string;
    '48': string;
    '60': string;
    '19.2': string;
    '17.92': string;
    '14.4': string;
 *   };
 *   space: {
    '1': string;
    '20': string;
    '24': string;
    '30': string;
    '40': string;
    '48': string;
    '56': string;
    '60': string;
    '70': string;
    '78': string;
    '84': string;
    '100': string;
    '287': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    lg: string;
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
    "primary": "#c00121",
    "secondary": "#fff8e7",
    "accent": "#146ff8",
    "background": "#fff8e7",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#66635c",
    "neutral300": "#808080",
    "neutral400": "#f0f0f0",
    "neutral500": "#1f2533",
    "neutral600": "#949494",
    "neutral700": "#c9c9c9",
    "neutral800": "#fee9e8"
  },
  "fonts": {
    "body": "'Roboto', sans-serif"
  },
  "fontSizes": {
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "22": "22px",
    "28": "28px",
    "32": "32px",
    "40": "40px",
    "48": "48px",
    "60": "60px",
    "19.2": "19.2px",
    "17.92": "17.92px",
    "14.4": "14.4px"
  },
  "space": {
    "1": "1px",
    "20": "20px",
    "24": "24px",
    "30": "30px",
    "40": "40px",
    "48": "48px",
    "56": "56px",
    "60": "60px",
    "70": "70px",
    "78": "78px",
    "84": "84px",
    "100": "100px",
    "287": "287px"
  },
  "radii": {
    "sm": "3px",
    "md": "8px",
    "xl": "24px",
    "full": "50px"
  },
  "shadows": {
    "sm": "rgba(19, 110, 248, 0.3) 0px 0px 0px 5px",
    "lg": "rgba(8, 19, 79, 0.16) 0px 4px 13.333px 0px"
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
    "primary": {
      "main": "#c00121",
      "light": "hsl(350, 99%, 53%)",
      "dark": "hsl(350, 99%, 23%)"
    },
    "secondary": {
      "main": "#fff8e7",
      "light": "hsl(42, 100%, 95%)",
      "dark": "hsl(42, 100%, 80%)"
    },
    "background": {
      "default": "#fff8e7",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#1f2533"
    }
  },
  "typography": {
    "fontFamily": "'Inter', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "32px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "700",
      "lineHeight": "38.0016px"
    },
    "h3": {
      "fontSize": "22px",
      "fontWeight": "400",
      "lineHeight": "35.75px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(19, 110, 248, 0.3) 0px 0px 0px 5px",
    "rgba(8, 19, 79, 0.16) 0px 4px 13.333px 0px"
  ]
};

export default theme;

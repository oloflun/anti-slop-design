// React Theme — extracted from https://aveon.framer.website/
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '11': string;
    '12': string;
    '13': string;
    '14': string;
    '16': string;
    '22': string;
    '36': string;
    '44': string;
    '60': string;
    '80': string;
    '144': string;
 *   };
 *   space: {
    '1': string;
    '40': string;
    '60': string;
    '66': string;
    '80': string;
    '100': string;
    '120': string;
    '240': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
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
    "primary": "#0000ee",
    "secondary": "#b8845c",
    "accent": "#2c2218",
    "background": "#e8e0d6",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#1a1a1a",
    "neutral200": "#e5ddd4",
    "neutral300": "#ffffff",
    "neutral400": "#767676",
    "neutral500": "#3e3228"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif"
  },
  "fontSizes": {
    "11": "11px",
    "12": "12px",
    "13": "13px",
    "14": "14px",
    "16": "16px",
    "22": "22px",
    "36": "36px",
    "44": "44px",
    "60": "60px",
    "80": "80px",
    "144": "144px"
  },
  "space": {
    "1": "1px",
    "40": "40px",
    "60": "60px",
    "66": "66px",
    "80": "80px",
    "100": "100px",
    "120": "120px",
    "240": "240px"
  },
  "radii": {
    "sm": "5px",
    "md": "10px",
    "lg": "16px",
    "xl": "20px",
    "full": "999px"
  },
  "shadows": {
    "sm": "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "xs": "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
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
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "secondary": {
      "main": "#b8845c",
      "light": "hsl(26, 39%, 69%)",
      "dark": "hsl(26, 39%, 39%)"
    },
    "background": {
      "default": "#e8e0d6",
      "paper": "#1a1512"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#f2ede7"
    }
  },
  "typography": {
    "fontFamily": "'Inter Display', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "600",
      "lineHeight": "36px"
    },
    "h3": {
      "fontSize": "22px",
      "fontWeight": "600",
      "lineHeight": "24.2px"
    }
  },
  "shape": {
    "borderRadius": 10
  },
  "shadows": [
    "rgb(242, 237, 231) 0px 0px 0px 2px",
    "rgb(184, 132, 92) 0px 0px 0px 2px",
    "rgba(184, 132, 92, 0.8) 0px 0px 0px 3px",
    "rgb(255, 255, 255) 0px 0px 0px 2px",
    "rgb(0, 0, 0) 0px 0px 0px 1px inset"
  ]
};

export default theme;

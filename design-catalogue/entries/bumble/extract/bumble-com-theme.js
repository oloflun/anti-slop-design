// React Theme — extracted from https://bumble.com
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '15': string;
    '16': string;
    '17': string;
    '18': string;
    '20': string;
    '24': string;
    '32': string;
    '34': string;
    '40': string;
    '49': string;
    '68': string;
 *   };
 *   space: {
    '1': string;
    '6': string;
    '20': string;
    '32': string;
    '40': string;
    '48': string;
    '60': string;
 *   };
 *   radii: {
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    md: string;
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
    "primary": "#ffdb5b",
    "secondary": "#0000ee",
    "accent": "#fff386",
    "background": "#ffdb5b",
    "foreground": "#343333",
    "neutral50": "#202020",
    "neutral100": "#575656",
    "neutral200": "#343333",
    "neutral300": "#ffffff",
    "neutral400": "#f3f3f3"
  },
  "fonts": {
    "body": "'BumbleSans', sans-serif"
  },
  "fontSizes": {
    "15": "15px",
    "16": "16px",
    "17": "17px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "32": "32px",
    "34": "34px",
    "40": "40px",
    "49": "49px",
    "68": "68px"
  },
  "space": {
    "1": "1px",
    "6": "6px",
    "20": "20px",
    "32": "32px",
    "40": "40px",
    "48": "48px",
    "60": "60px"
  },
  "radii": {
    "md": "9px",
    "lg": "16px",
    "xl": "24px",
    "full": "1000px"
  },
  "shadows": {
    "sm": "rgba(255, 255, 255, 0) 0px 0px 0px 0px",
    "md": "rgba(32, 32, 32, 0.12) 0px 1px 8px 0px"
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
      "main": "#ffdb5b",
      "light": "hsl(47, 100%, 83%)",
      "dark": "hsl(47, 100%, 53%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#ffdb5b",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#343333",
      "secondary": "#202020"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "32px",
      "fontWeight": "700",
      "lineHeight": "48px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "24px"
    }
  },
  "shape": {
    "borderRadius": 9
  },
  "shadows": [
    "rgba(255, 255, 255, 0) 0px 0px 0px 0px",
    "rgba(32, 32, 32, 0.12) 0px 1px 8px 0px"
  ]
};

export default theme;

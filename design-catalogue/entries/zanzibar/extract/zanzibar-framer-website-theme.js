// React Theme — extracted from https://zanzibar.framer.website
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
    '12': string;
    '14': string;
    '16': string;
    '17': string;
    '18': string;
    '36': string;
    '144': string;
    '14.4': string;
 *   };
 *   space: {
    '1': string;
    '32': string;
    '48': string;
    '64': string;
    '80': string;
    '96': string;
    '112': string;
    '180': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
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
    "primary": "#fffaf6",
    "secondary": "#0000ee",
    "accent": "#f1efe5",
    "background": "#100c08",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#100c08",
    "neutral200": "#767676"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "17": "17px",
    "18": "18px",
    "36": "36px",
    "144": "144px",
    "14.4": "14.4px"
  },
  "space": {
    "1": "1px",
    "32": "32px",
    "48": "48px",
    "64": "64px",
    "80": "80px",
    "96": "96px",
    "112": "112px",
    "180": "180px"
  },
  "radii": {
    "sm": "4px",
    "md": "10px",
    "lg": "16px",
    "full": "100px"
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
      "main": "#fffaf6",
      "light": "hsl(27, 100%, 95%)",
      "dark": "hsl(27, 100%, 83%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#100c08",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Inter', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "1000",
      "lineHeight": "43.2px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "normal"
    },
    "body2": {
      "fontSize": "14.4px",
      "fontWeight": "1000",
      "lineHeight": "18px"
    }
  },
  "shape": {
    "borderRadius": 7
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
  ]
};

export default theme;

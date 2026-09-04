// React Theme — extracted from https://archline.framer.website/
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '16': string;
    '20': string;
    '24': string;
    '28': string;
    '32': string;
    '40': string;
    '64': string;
    '72': string;
    '100': string;
    '18.08': string;
    '14.08': string;
    '12.96': string;
 *   };
 *   space: {
    '2': string;
    '48': string;
    '56': string;
    '80': string;
    '100': string;
    '120': string;
    '136': string;
    '150': string;
    '156': string;
    '164': string;
    '200': string;
    '240': string;
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
    "primary": "#fffcf3",
    "secondary": "#0000ee",
    "accent": "#33261f",
    "background": "#000000",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#252324"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "20": "20px",
    "24": "24px",
    "28": "28px",
    "32": "32px",
    "40": "40px",
    "64": "64px",
    "72": "72px",
    "100": "100px",
    "18.08": "18.08px",
    "14.08": "14.08px",
    "12.96": "12.96px"
  },
  "space": {
    "2": "2px",
    "48": "48px",
    "56": "56px",
    "80": "80px",
    "100": "100px",
    "120": "120px",
    "136": "136px",
    "150": "150px",
    "156": "156px",
    "164": "164px",
    "200": "200px",
    "240": "240px"
  },
  "radii": {
    "sm": "3px",
    "md": "8px",
    "lg": "11px",
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
      "main": "#fffcf3",
      "light": "hsl(45, 100%, 95%)",
      "dark": "hsl(45, 100%, 83%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#000000",
      "paper": "#fffdfa"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "44.8px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "400",
      "lineHeight": "39.2px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
  ]
};

export default theme;
